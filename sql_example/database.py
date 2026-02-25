#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：fastapi_start 
@File    ：database.py
@Author  ：zhanghao
@Date    ：2026/2/25 16:34 
'''
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import create_engine, Integer, String


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))


DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(engine)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)
