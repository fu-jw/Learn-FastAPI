import uvicorn
import time

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/index")
async def index():
    return {"Hello": "World"}


# 创建中间件
# request：请求对象
# call_next：回调函数
# 可以创建多个，调用时，按照创建倒序
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    # 一些处理 ...
    start_time = time.time()
    # 处理请求
    response = await call_next(request)
    # 一些处理 ...
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    # 返回请求处理结果
    return response


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
