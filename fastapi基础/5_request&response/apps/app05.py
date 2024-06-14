from fastapi import APIRouter, File, UploadFile
from typing import List

app05 = APIRouter()


# 单文件
@app05.post("/file/")
# 类型为bytes，以字节流形式接受文件
async def create_file(file: bytes = File()):
    print(file)  # b'\xff\xd8...'，以字节形式输出
    return {"file_size": len(file)}


# 多文件
@app05.post("/files/")
# 类型为bytes，以字节流形式接受文件
async def create_files(files: List[bytes] = File()):
    return {"file_size": len(files)}  # 文件个数


# File 以字节流形式接受文件，不适合大文件

# 以文件句柄的形式接收文件，更简单常用【推荐】
@app05.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}


@app05.post("/uploadfiles/")
async def create_upload_files(files: List[UploadFile]):
    return {"filename": files.filename}
