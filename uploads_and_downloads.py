#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start
@File    ：uploads_and_downloads.py
@Author  ：zhanghao
@Date    ：2026/2/25 20:46
@desc    : 上传文件
'''
import os
import shutil

from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

UPLOAD_DIR = "./uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@app.post("/uploadfile")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)  # type: ignore
    return {"filename": file.filename, "location": file_location}


@app.get("/downloadfile/{filename}")
async def download_file(filename: str):
    if not (os.path.exists(os.path.join(UPLOAD_DIR, filename))):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(os.path.join(UPLOAD_DIR, filename), filename=filename)
