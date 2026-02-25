#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：main.py
@Author  ：zhanghao
@Date    ：2026/2/25 14:52 
'''
import router_example
from fastapi import FastAPI

app = FastAPI()

app.include_router(router_example.router)


@app.get("/")
async def read_root():
    return {"message": "Hello World"}
