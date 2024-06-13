from fastapi import APIRouter

user = APIRouter()


@user.post('/user/login')
def user_login():
    return {"user": "login"}


@user.post('/user/reg')
def user_reg():
    return {"user": "reg"}
