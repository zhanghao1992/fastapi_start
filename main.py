#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：main.py
@Author  ：zhanghao
@Date    ：2026/2/25 14:52 
'''
import json

from fastapi import FastAPI
from pydantic import BaseModel
from nosql_example.database import users_collection

app = FastAPI()


class User(BaseModel):
    name: str
    email: str


class UserResponse(User):
    id: str


@app.get("/users")
async def read_users() -> list[User]:
    return [user for user in users_collection.find()]


@app.post("/user")
async def create_user(user: User):
    result = users_collection.insert_one(user.model_dump(exclude_none=True))
    user_response = UserResponse(
        id=str(result.inserted_id),
        *user.model_dump()
    )
    return user_response
