#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：database.py
@Author  ：zhanghao
@Date    ：2026/2/25 17:41 
'''
from pymongo import MongoClient

client = MongoClient("mongodb://root:StrongPassword123!@115.190.179.81:27017/admin?authSource=admin")

database = client['fastapi_start']

users_collection = database["users"]
