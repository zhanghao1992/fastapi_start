#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：main.py
@Author  ：zhanghao
@Date    ：2026/2/25 15:14 
'''
from fastapi import FastAPI

app = FastAPI()


@app.get("/books/{book_id}")
async def read_book(book_id: int):
    return {"book_id": book_id, "title": "The Greate Gatsby", "author": "F.Scott Fitzgerald"}
