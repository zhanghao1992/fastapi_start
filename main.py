#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：main.py
@Author  ：zhanghao
@Date    ：2026/2/25 14:52 
'''
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
