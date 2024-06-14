from fastapi import APIRouter, Form

app04 = APIRouter()


@app04.post("/login/")
# 声明表单体要显式使用 Form，否则，FastAPI 会把该参数当作查询参数或请求体（JSON）参数。
async def login(username: str = Form(), password: str = Form()):
    return {"username": username, "password": password}
