from typing import List

from fastapi import APIRouter
from pydantic import BaseModel, Field, field_validator
from typing import Optional

app03 = APIRouter()


# 定义请求体数据类型
# 继承BaseModel，由pydantic进行数据类型校验
class User(BaseModel):
    # 可以有默认值
    name: str = "root"
    # 可以有数据范围，默认值，最大最小值
    age: int = Field(default=20, gt=10, le=100, max=100, min=10)
    friends: Optional[List[int]]
    # 可以使用正则表达式
    # other: str = Field(pattern="^a")
    other: str

    # validator 已经废弃
    # cls 类型对象
    # v 字段值
    @field_validator('other')# 要校验的字段
    def validate_name(cls, v):
        # 使用断言，如果true就继续
        # 否则抛出异常提示：Assertion failed, 只能字母
        assert v.isalpha(), "只能字母"
        return v


# 请求体数据
@app03.post("/data")
async def data(user: User):
    print(user, type(user))  # name='fredo' age=20 friends=[1, 2, 3] <class 'apps.app03.User'>
    print(user.name)  # fredo
    print(user.dict())  # {'name': 'fredo', 'age': 20, 'friends': [1, 2, 3]}

    return {}
