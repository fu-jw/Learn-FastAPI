from fastapi import FastAPI
import uvicorn
from apps.shop.urls import shop
from apps.user.urls import user

app = FastAPI()
app.include_router(shop, prefix="/shop", tags=["购物中心"])
app.include_router(user, tags=["用户中心"])

if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, reload=True)
