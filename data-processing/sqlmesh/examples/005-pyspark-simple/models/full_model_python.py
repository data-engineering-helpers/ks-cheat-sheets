import typing as t
from datetime import datetime

import pandas as pd
#from sqlglot import exp

from sqlmesh import ExecutionContext, model
from sqlmesh.core.model import ModelKindName


@model(
    "sqlmesh_example.full_model_python",
    kind=dict(name=ModelKindName.FULL),
    cron="@daily",
    columns={
        "id": "int",
        "name": "text",
        #"country": "text",
    },
    column_descriptions={
        "id": "Unique ID",
        "name": "Name corresponding to the ID",
    },
    grain=["id"],
    audits=[
        ("not_null", {"columns": ["id"]}),
    ],
    description="Simple Python model",
)
def execute(
    context: ExecutionContext,
    start: datetime,
    end: datetime,
    execution_time: datetime,
    **kwargs: t.Any,
) -> pd.DataFrame:

    df = pd.DataFrame([{"id": 1, "name": "Laura"}, {"id": 2, "name": "John"}, {"id": 3, "name": "Lucie"}])
    #df = pd.DataFrame([{"id": 1, "name": "Laura", "country": "DE"}, {"id": 2, "name": "John", "country": "UK"}, {"id": 3, "name": "Lucie", "country": "FR"}])
    
    return df

