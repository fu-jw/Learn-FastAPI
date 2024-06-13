from fastapi import APIRouter

app01 = APIRouter()


@app01.get("/")
async def index():
    return {"Hello": "World"}


# 带参路径
@app01.get("/items/{id}")
async def get_items(id):
    return {"get_items": id}


# 带参路径，有参数类型
@app01.get("/item/{id}")
# 参数类型声明为 int 【推荐】
async def get_item(id: int):
    return {"get_item": id}


"""
注意：
1. 数据行中获取的数据是字符串，但是fastapi可以自动进行数据转换
2. 可以进行数据类型校验
    比如，访问： http://127.0.0.1:8000/item/foo 时，“foo” 无法转换成int,就会报错
3. 顺序很重要。同时匹配到多个路径时，按照声明顺序优先匹配，即先声明者先匹配
"""
