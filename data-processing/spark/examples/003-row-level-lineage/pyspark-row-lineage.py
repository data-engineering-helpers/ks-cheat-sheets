import re
import typing as T

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
    # Column manipulations
    #################################
    # Select
    # -------------------------------
    def row_lineage_select(self: DataFrame, *cols: ColumnOrName) -> DataFrame:
        return self.select(
            *cols,
            *[row_ids_col for row_ids_col in set(self.columns) & set(row_ids_columns)]
        )
    DataFrame.select = row_lineage_select
    # TODO: check if window function can be used within select statement (probably yes)

    # with_column
    # -------------------------------
    def replace_word_before_over(original_string, replacement):
        """
        WARNING: AI GENERATED, TO BE CHECKED!
        Replaces the first word in a string of the form "word OVER (another_word)".

        Args:
            original_string (str): The string to modify.
            replacement (str): The word to replace the first word with.

        Returns:
            str: The new string with the word replaced.
        """
        # The regex pattern:
        # \b(\w+)\b : Matches and captures a word (group 1)
        # (?=\sOVER\s\(.+\)) : Positive lookahead to ensure it's followed by " OVER (some_text)"
        pattern = r"\b(\w+)\b(?=\sOVER\s\(.+\))"

        # Use re.sub to replace the captured word
        return re.sub(pattern, replacement, original_string)
    
    def row_lineage_with_column(self: DataFrame, colName: str, col: Column) -> DataFrame:
        col_sql_expr = str(col._jc.toString())
        if "PARTITION BY" in col_sql_expr:
            return reduce(
                lambda df, row_ids_col: df.withColumn(
                    row_ids_col, 
                    F.expr(replace_word_before_over(col_sql_expr, f"array_distinct(flatten(collect_list({row_ids_col})))")).alias(row_ids_col)
                ),
                set(self.columns) & set(row_ids_columns), 
                self.withColumn(colName, col)
            )
        return self.withColumn(colName, col)
    DataFrame.withColumn = row_lineage_with_column

    #################################
    # Aggregations
    #################################

    # Group By
    # -------------------------------
    def row_lineage_agg(self: GroupedData, *exprs: T.Union[Column, T.Dict[str, str]]) -> DataFrame:
        return self.agg(
            *exprs,
            *[
                F.array_distinct(
                    F.flatten(
                        F.collect_list(row_ids_col)
                    )
                ).alias(row_ids_col)
                for row_ids_col in set(self._df.columns) & set(row_ids_columns)
            ]
        )
    GroupedData.agg = row_lineage_agg

    # TODO: leftanti / leftsemi could be problematic...
