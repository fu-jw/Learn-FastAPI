from fastapi import FastAPI

app = FastAPI()


@app.post("/item")
async def item():
    return {"message": "Hello World"}


@app.post("/item1", tags=["item1-tag1", "item1-tag2"])
async def item1():
    return {"message": "Hello World"}


@app.post("/item2", summary="这是summary，接口信息概述")
async def item2():
    return {"message": "Hello World"}


@app.post("/item3",
          summary="这是summary，接口信息概述",
          description="这是description，接口信息详细描述"
          )
async def item3():
    return {"message": "Hello World"}


@app.post("/item4",
          summary="这是summary，接口信息概述",
          description="这是description，接口信息详细描述",
          deprecated=True
          )
async def item4():
    return {"message": "Hello World"}
