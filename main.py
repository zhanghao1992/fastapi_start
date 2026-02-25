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


@app.get("/books/{book_id}")  # http://127.0.0.1:8000/book/11
async def read_book(book_id: int):
    return {"book_id": book_id, "title": "The Greate Gatsby", "author": "F.Scott Fitzgerald"}


@app.get("/authors/{author_id}")  # http://127.0.0.1:8000/authors/1
async def read_author(author_id: int):
    return {
        "author_id": author_id,
        "name": "Ernest Hemingway"
    }


@app.get("/books")  # http://127.0.0.1:8000/books?year=2025
async def read_books(year: int = None):
    if year:
        return {
            "year": year,
            "books": ["Book 1", "Book 2"]
        }
    return {"books": ["All Books"]}
