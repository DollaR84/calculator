"""
Main running module for the calculator.

created on 09.06.2020

@author: Ruslan Dolovanyuk

"""

from fastapi import FastAPI
from fastapi import HTTPException

from config import Settings

from database import Database

from models import ParamsModel, ResultModel, OperationModel


app = FastAPI(title='Calculator')
settings = Settings()
db = Database(settings.db)


@app.post(
    "/add",
    response_description="Addition method two parameters",
    description="Return result operation a + b",
    response_model=ResultModel,
)
async def add(params: ParamsModel):
    res = ResultModel(result=(params.a + params.b))
    await db.add(OperationModel(operation=add.__name__, params=params, result=res))
    return res


@app.post(
    "/sub",
    response_description="Subtraction method two parameters",
    description="Return result operation a - b",
    response_model=ResultModel,
)
async def sub(params: ParamsModel):
    res = ResultModel(result=(params.a - params.b))
    await db.add(OperationModel(operation=sub.__name__, params=params, result=res))
    return res


@app.post(
    "/mul",
    response_description="Multiplication method two parameters",
    description="Return result operation a * b",
    response_model=ResultModel,
)
async def mul(params: ParamsModel):
    res = ResultModel(result=(params.a * params.b))
    await db.add(OperationModel(operation=mul.__name__, params=params, result=res))
    return res


@app.post(
    "/div",
    response_description="Division method two parameters",
    description="Return result operation a / b",
    response_model=ResultModel,
)
async def div(params: ParamsModel):
    try:
        res = ResultModel(result=(params.a / params.b))
    except ZeroDivisionError:
        raise HTTPException(404, "error division by zero")
    await db.add(OperationModel(operation=div.__name__, params=params, result=res))
    return res
