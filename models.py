#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：models.py
@Author  ：zhanghao
@Date    ：2026/2/25 15:24 
'''
from pydantic import BaseModel, Field


class Book(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    author: str = Field(..., min_length=1, max_length=50)
    year: int = Field(..., gt=1900, lt=2100)
