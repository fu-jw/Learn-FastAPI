from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# 带参路径
@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}


@app.get("/item/{id}")
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
