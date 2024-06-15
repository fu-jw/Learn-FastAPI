import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')  # 对应 templates 文件夹


@app.get("/index")
async def index():
    return {"Hello": "World"}


@app.get("/")
async def index(request: Request):
    # 模拟数据
    name = "Fredo"
    age = 20
    books = ["数据结构与算法", "Java编程思想", "Linux是如何运行的", "图解TCP/IP"]
    info = {"name": name, "age": age, "books": books}
    pai = 3.141592653589793

    return templates.TemplateResponse(
        "index.html",  # 模板文件
        {
            "request": request,  # 必须包含请求对象
            "name": name,
            "age": age,
            "books": books ,
            "info": info,
            "pai": pai
        }
    )


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
