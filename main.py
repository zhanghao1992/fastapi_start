#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：main.py
@Author  ：zhanghao
@Date    ：2026/2/25 14:52 
'''
import json

# import router_example
from fastapi import FastAPI, HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel
from starlette.responses import JSONResponse, PlainTextResponse

from models import Book

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": "Oops! Something went wrong"},
    )


@app.exception_handler(RequestValidationError)
async def http_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(
        "This is a plain text response:" f"\n{json.dumps(exc.errors(), indent=2)}",
        status_code=status.HTTP_400_BAD_REQUEST
    )


# app.include_router(router_example.router)


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


class BookResponse(BaseModel):
    title: str
    author: str


@app.get("/allbooks", response_model=list[BookResponse])
async def read_all():
    return [
        {
            "id": 1,
            "title": "1984",
            "author": "George Orwell",
        },
        {
            "id": 1,
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
        }
    ]


@app.post("/book")
async def create_book(book: Book):
    return book


@app.get("/error_endpoint")
async def error_endpoint():
    raise HTTPException(status_code=400, detail="Oops!")
