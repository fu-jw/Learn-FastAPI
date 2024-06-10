# 从fastapi包中引入 FastAPI 类
# FastAPI 是直接从 Starlette 继承的类，可以使用所有的 Starlette 的功能
from fastapi import FastAPI

# 创建一个 FastAPI 实例，名称为 app
# 这个实例将是创建你所有 API 的主要交互对象
# 同时与启动命令对应
app = FastAPI()


# 定义一个路径操作装饰器
@app.get("/")
# 定义路径操作函数
async def root():
    return {"message": "Hello World"}


"""
执行命令：uvicorn main:app --reload

含义如下:
main：main.py 文件（一个 Python「模块」）。
app：在 main.py 文件中通过 app = FastAPI() 创建的对象。
--reload：让服务器在更新代码后重新启动。仅在开发时使用该选项。
"""