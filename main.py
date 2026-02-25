#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：main.py
@Author  ：zhanghao
@Date    ：2026/2/25 14:52
@desc    : mongodb
'''
import json

from bson import ObjectId
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, field_validator
from nosql_example.database import users_collection

app = FastAPI()


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator('age')
    def validate_age(cls, v):
        if v < 18 or v > 100:
            raise HTTPException(status_code=400, detail="Age must be between 18 and 100")
        return v


class UserResponse(UserCreate):
    id: str


@app.get("/users")
async def read_users() -> list[UserCreate]:
    return [user for user in users_collection.find()]


@app.post("/user")
async def create_user(user: UserCreate):
    result = users_collection.insert_one(user.model_dump(exclude_none=True))
    user_response = UserResponse(
        id=str(result.inserted_id),
        **user.model_dump()
    )
    return user_response


@app.get('/user')
async def get_user(user_id: str) -> UserResponse:
    db_user = users_collection.find_one({'_id': ObjectId(user_id) if ObjectId.is_valid(user_id) else None})
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    # user_response = UserResponse(
    #     id=str(db_user['_id']),
    #     **db_user
    # )
    # return user_response
    db_user["id"] = str(db_user["_id"])
    return db_user
