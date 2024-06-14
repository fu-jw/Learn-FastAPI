from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from typing import Optional, List

app07 = APIRouter()


class UserIn(BaseModel):
    name: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


class UserOut(BaseModel):
    name: str
    email: EmailStr
    full_name: Optional[str] = None


# 自动将输出数据转换成UserOut类型，无password
@app07.post("/reg/", response_model=UserOut)
async def creat_user(user: UserIn):
    # do something ...
    return user


########################################################################
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: float = 10.5
    tags: List[str] = None


# 模拟数据库中的数据
items = {
    "foo": {"name": "foo", "price": 123.40},
    "bar": {"name": "bar", "description": "bar description", "price": 67.40, "tax": 23.40},
    "baz": {"name": "baz", "description": None, "price": 67.40, "tax": 23.40, "tags": []},
}

# @app07.post("/reg/{item_id}", response_model=Item)
# async def read_item(item_id: str):
#     return items[item_id]

# 默认情况返回类型 Item 中所有字段，例如：
"""
{
  "name": "foo",
  "description": null,
  "price": 123.4,
  "tax": 10.5,
  "tags": null
}
"""


# response_model_exclude_unset：不包含未设置值，即按照实际数据 有啥返回啥(不会根据数据类型添加其他字段)
@app07.post("/reg/{item_id}", response_model=Item, response_model_exclude_unset=True)
async def read_item(item_id: str):
    return items[item_id]


"""
{
  "name": "foo",
  "price": 123.4
}
"""


# response_model_exclude_defaults：不包含未默认值
# response_model_exclude_none：不包含 None 值

##################################################################################
# response_model_include：只包含某些字段
@app07.post("/reg/{item_id}", response_model=Item, response_model_include={"name", "price"})
async def read_item(item_id: str):
    return items[item_id]


# response_model_exclude：不包含某些字段
@app07.post("/reg/{item_id}", response_model=Item, response_model_exclude={"tax", "tags"})
async def read_item(item_id: str):
    return items[item_id]
