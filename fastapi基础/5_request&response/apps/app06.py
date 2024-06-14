from fastapi import APIRouter, Request

app06 = APIRouter()


@app06.post("/items/")
async def items(request: Request):

    return {
        "URL": request.url,
        "Host": request.client.host,
        "请求宿主": request.headers.get("user-agent"),
        "cookie": request.cookies.get("cookie"),
        }

