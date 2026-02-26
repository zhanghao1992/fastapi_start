#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start
@File    ：mongodb.py
@Author  ：zhanghao
@Date    ：2026/2/25 17:25
@Description: MongoDB数据库配置
'''
from pymongo import MongoClient
from typing import Optional

# MongoDB连接配置
MONGODB_URL = "mongodb://root:StrongPassword123!@115.190.179.81:27017/admin?authSource=admin"

# 创建MongoDB客户端
client: Optional[MongoClient] = None

def get_database():
    """获取数据库连接"""
    global client
    if client is None:
        client = MongoClient(MONGODB_URL)
    return client.admin  # 使用admin数据库，或修改为你的数据库名

def get_collection(collection_name: str):
    """获取集合（表）"""
    db = get_database()
    return db[collection_name]

def close_mongodb_connection():
    """关闭MongoDB连接"""
    global client
    if client is not None:
        client.close()
        client = None


# User模型的MongoDB操作
class UserDB:
    """用户数据库操作类"""

    @staticmethod
    def get_collection():
        """获取user集合"""
        return get_collection("user")

    @staticmethod
    def create_user(name: str, email: str) -> str:
        """创建用户"""
        collection = UserDB.get_collection()
        result = collection.insert_one({
            "name": name,
            "email": email
        })
        return str(result.inserted_id)

    @staticmethod
    def get_all_users():
        """获取所有用户"""
        collection = UserDB.get_collection()
        return list(collection.find({}, {"_id": 0}))

    @staticmethod
    def get_user_by_email(email: str):
        """根据邮箱获取用户"""
        collection = UserDB.get_collection()
        return collection.find_one({"email": email}, {"_id": 0})

    @staticmethod
    def update_user(email: str, name: Optional[str] = None):
        """更新用户信息"""
        collection = UserDB.get_collection()
        update_data = {}
        if name:
            update_data["name"] = name
        collection.update_one(
            {"email": email},
            {"$set": update_data}
        )

    @staticmethod
    def delete_user(email: str):
        """删除用户"""
        collection = UserDB.get_collection()
        collection.delete_one({"email": email})


# 测试连接
if __name__ == "__main__":
    try:
        # 测试连接
        db = get_database()
        print("✓ MongoDB连接成功!")
        print(f"✓ 数据库列表: {client.list_database_names()}")

        # 测试创建用户
        UserDB.create_user("测试用户", "test@example.com")
        print("✓ 创建测试用户成功!")

        # 查询所有用户
        users = UserDB.get_all_users()
        print(f"✓ 当前用户数量: {len(users)}")
        for user in users:
            print(f"  - {user['name']}: {user['email']}")

        close_mongodb_connection()
        print("✓ 连接已关闭")

    except Exception as e:
        print(f"✗ 连接失败: {e}")
