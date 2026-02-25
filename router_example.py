#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：router_example.py
@Author  ：zhanghao
@Date    ：2026/2/25 15:08 
'''
from fastapi import APIRouter

router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
