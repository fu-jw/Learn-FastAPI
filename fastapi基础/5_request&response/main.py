from fastapi import FastAPI
import uvicorn
from apps.app01 import app01


app = FastAPI()
app.include_router(app01, tags=["请求与响应"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
