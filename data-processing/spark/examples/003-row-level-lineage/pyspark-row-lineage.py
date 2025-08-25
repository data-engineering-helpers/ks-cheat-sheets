import re
import typing as T
import functools

import pyspark.sql.functions as F
from pyspark.sql import (
    GroupedData,
    DataFrame, 
    Column
)
from pyspark.sql.window import (
    WindowSpec,
    Window
)
from contextlib import contextmanager
from functools import reduce

ColumnOrName = T.Union[Column, str]


def column_expr_validator(col: ColumnOrName) -> str:
    match col:
        case str():
            return col
        case Column():
            return str(col._jc)
        case _:
            raise ValueError(f"Invalid column expression: {col}")


def find_closing_parenthesis_idx(s: str) -> int:
    if s[0] != '(':
        return -1
    stack = 0
    for i, c in enumerate(s):
        if c == '(':
            stack += 1
        elif c == ')':
            stack -= 1
            if stack == 0:
                return i
    return -1


def find_partitions_expr(col: ColumnOrName) -> T.List[str]:
    col = column_expr_validator(col)
    over_positions = list(re.finditer(r' OVER ', col))
    l = []
    for i, _ in enumerate(over_positions):
        j = find_closing_parenthesis_idx(col[over_positions[i].end():over_positions[i+1].start() if over_positions[i+1:] else None])
        l.append(col[over_positions[i].start():over_positions[i].end() + j + 1])
    return l


def row_ids_column(df: DataFrame) -> str:
    return f"__row_ids_{id(df)}"

@contextmanager
def row_lineage(*dataframes: DataFrame):
    try:
        for df in dataframes:
            df = df.withColumn(row_ids_column(df), F.array(F.monotonically_increasing_id()))

        pyspark_monkey_patch(*[row_ids_column(df) for df in dataframes])

        yield tuple(dataframes)
    finally:
        for df in dataframes:
            df = df.drop(columns=[row_ids_column(df)])


def pyspark_monkey_patch(*row_ids_columns: str):
    #################################
    # Aggregations
    #################################
    # Aggregation column
    # -------------------------------
    def get_aggregation_column(row_ids_col: ColumnOrName) -> Column:
        return F.array_distinct(
            F.flatten(
                F.collect_list(row_ids_col)
            )
        )
    
    def get_aggregation_expr(row_ids_col: ColumnOrName) -> str:
        return str(get_aggregation_column(row_ids_col)._jc)
    
    def aggregate_row_ids(col: ColumnOrName, row_ids_col: str) -> Column:
        return F.expr(
            functools.reduce(
                lambda c, partition: f"({get_aggregation_expr(c)}){partition}",
                find_partitions_expr(col),
                row_ids_col
            )
        ).alias(row_ids_col)

    # Group By
    # -------------------------------
    def row_lineage_agg(self: GroupedData, *exprs: T.Union[Column, T.Dict[str, str]]) -> DataFrame:
        return self.agg(
            *exprs,  # TODO: expressions can contain nested window functions
            *[
                get_aggregation_column(row_ids_col).alias(row_ids_col)
                for row_ids_col in set(self._df.columns) & set(row_ids_columns)
            ]
        )
    GroupedData.agg = row_lineage_agg

    #################################
    # Column manipulations
    #################################
    # Select
    # -------------------------------
    def row_lineage_select(self: DataFrame, *cols: ColumnOrName) -> DataFrame:
        partitioned_columns = [col for col in cols if "OVER" in column_expr_validator(col)]
        output_df = self.select(
            *cols,
            *[row_ids_col for row_ids_col in set(self.columns) & set(row_ids_columns)],
        )
        if partitioned_columns:
            return functools.reduce(
                lambda df, partitioned_col: ...,  # TODO: implement
                partitioned_columns,
                output_df
            )
        return output_df
    DataFrame.select = row_lineage_select
    # TODO: selectExpr
    # TODO: aggregation functions can be used without groupBy or window functions e.g., df.select(F.sum("col1"))

    # withColumn
    # -------------------------------
    def row_lineage_with_column(self: DataFrame, colName: str, col: Column) -> DataFrame:
        if "OVER" in str(col._jc):
            return functools.reduce(
                lambda df, row_id_col: df.withColumn(row_id_col, aggregate_row_ids(colName, row_id_col)),
                row_ids_columns,
                self.withColumn(colName, col)
            )
        return self.withColumn(colName, col)
    DataFrame.withColumn = row_lineage_with_column

    #################################
    # Joins
    #################################
    # TODO: when joining 2 dataframes, the same row_ids_columns could be present in both => we should take the union!
    # TODO: leftanti / leftsemi could be problematic...    
