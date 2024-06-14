from fastapi import APIRouter
from typing import Union
from typing import Optional

app02 = APIRouter()


# 带参路径
@app02.get("/jobs")
async def get_item(kd, xl: str, gj: str = "3-5"):
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj
    }


@app02.get("/jobs")
async def get_items(kd: Union[str, None], xl: Optional[str], gj: str = "3-5"):
    return {
        "kd": kd,
        "xl": xl,
        "gj": gj
    }
