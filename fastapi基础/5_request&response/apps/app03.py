from fastapi import APIRouter
from typing import Union
from typing import Optional

app03 = APIRouter()


# 带参路径
@app03.post("/data")
async def data():
    return {

    }
