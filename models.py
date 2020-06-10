"""
Models module for the calculator.

created on 09.06.2020

@author: Ruslan Dolovanyuk

"""

from pydantic import BaseModel
from pydantic import Field


class ParamsModel(BaseModel):
    """Params model"""

    a: int
    b: int


class ResultModel(BaseModel):
    """Result model"""

    result: float


class OperationModel(BaseModel):
    """Operation model"""

    operation: str = Field("", title="Operation method", description="Name operation of the calculating", max_length=3)
    params: ParamsModel
    result: ResultModel
