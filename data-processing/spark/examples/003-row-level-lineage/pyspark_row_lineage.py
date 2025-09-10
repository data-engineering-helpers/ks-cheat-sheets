import re
import typing as T
import functools

import pyspark.sql.functions as F
from pyspark.sql.classic.dataframe import DataFrame
from pyspark.sql import (
    GroupedData,
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
        patches = pyspark_monkey_patch(*[row_ids_column(df) for df in dataframes])
        dataframes = [
            df.withColumn(row_ids_column(df), F.array(F.monotonically_increasing_id()))
            for df in dataframes
        ]
        # dataframe_agg = DataFrame.agg
        # DataFrame.agg = patches["row_lineage_agg"]
        grouped_data_agg = GroupedData.agg
        GroupedData.agg = patches["row_lineage_agg"]
        dataframe_select = DataFrame.select
        DataFrame.select = patches["row_lineage_select"]
        dataframe_withColumn = DataFrame.withColumn
        DataFrame.withColumn = patches["row_lineage_with_column"]
        dataframe_join = DataFrame.join
        DataFrame.join = patches["row_lineage_join"]
        DataFrame.blame = patches["blame"]

        yield tuple(dataframes)
    finally:
        dataframes = [
            df.drop(*[row_ids_column(df)])
            for df in dataframes
        ]
        # DataFrame.agg = dataframe_agg
        GroupedData.agg = grouped_data_agg
        DataFrame.select = dataframe_select
        DataFrame.withColumn = dataframe_withColumn
        DataFrame.join = dataframe_join
        del DataFrame.blame


grouped_data_agg_original = GroupedData.agg
dataframe_withColumn_original = DataFrame.withColumn

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
                lambda c, partition: f"{get_aggregation_expr(c)}{partition}",
                find_partitions_expr(col),
                row_ids_col
            )
        ).alias(row_ids_col)

    # Group By
    # -------------------------------
    def row_lineage_agg(self: GroupedData, *exprs: T.Union[Column, T.Dict[str, str]]) -> DataFrame:
        return grouped_data_agg_original(
            self,
            *exprs,  # TODO: expressions can contain nested window functions
            *[
                get_aggregation_column(row_ids_col).alias(row_ids_col)
                for row_ids_col in set(self._df.columns) & set(row_ids_columns)
            ]
        )

    #################################
    # Column manipulations
    #################################
    # Select
    # -------------------------------
    def row_lineage_select(self: DataFrame, *cols: ColumnOrName) -> DataFrame:
        partitioned_columns = [col for col in cols if " OVER " in column_expr_validator(col)]
        output_df = self.select(
            *cols,
            *[row_ids_col for row_ids_col in set(self.columns) & set(row_ids_columns)],
        )
        return functools.reduce(
            lambda df, partitioned_col: functools.reduce(
                lambda df, row_id_col: df.withColumn(row_id_col, aggregate_row_ids(partitioned_col, row_id_col)),
                row_ids_columns,
                df
            ),
            partitioned_columns,
            output_df
        )
    # TODO: selectExpr
    # TODO: aggregation functions can be used without groupBy or window functions e.g., df.select(F.sum("col1"))

    # withColumn
    # -------------------------------
    def row_lineage_with_column(self: DataFrame, colName: str, col: Column) -> DataFrame:
        print("toto")
        if " OVER " in str(col._jc):
            print(col)
            toto = (set(self.columns) & set(row_ids_columns)).pop()
            print(aggregate_row_ids(col, toto))
            return functools.reduce(
                lambda df, row_id_col: dataframe_withColumn_original(df, row_id_col, aggregate_row_ids(col, row_id_col)),
                set(self.columns) & set(row_ids_columns),
                dataframe_withColumn_original(self, colName, col)
            )
        return dataframe_withColumn_original(self, colName, col)

    #################################
    # Joins
    #################################
    def row_lineage_join(self: DataFrame, other: DataFrame, on: T.Optional[T.Union[str, T.List[str], Column, T.List[Column]]] = None, how: T.Optional[str] = None) -> DataFrame:
        duplicated_row_ids_columns = [col for col in set(self.columns) & set(other.columns) if col in row_ids_columns]
        return functools.reduce(
            lambda df, col: df.withColumn(col + "_tmp", F.array_union(self[col], other[col])).drop(col).withColumnRenamed(col + "_tmp", col),
            duplicated_row_ids_columns,
            self.join(other, on=on, how=how)
        )
    # TODO: leftanti / leftsemi could be problematic...


    #################################
    # New methods
    #################################
    def blame(self: DataFrame, *traced_dataframes: DataFrame) -> T.Tuple[DataFrame]:
        self = dataframe_withColumn_original(self, row_ids_column(self), F.explode(self[row_ids_column(self)])).persist()
        return (
            traced_df.join(
                self,
                on=row_ids_column(traced_df),
                how="leftsemi"
            )
            for traced_df in traced_dataframes
        )
    return {
        "row_lineage_agg": row_lineage_agg,
        "row_lineage_select": row_lineage_select,
        "row_lineage_with_column": row_lineage_with_column,
        "row_lineage_join": row_lineage_join,
        "blame": blame
    }
