#!/usr/bin/python3
# -*- coding:utf-8 -*-
# __author__ = 'Albert'
# 利用 SQLAlchemy 的定义方式比较好，毕竟比较通用，可以做更多个性化的设置

from sqlalchemy import (
    Column,
    String,
    Integer,
    BigInteger,
    Date,
    DateTime,
    ForeignKey,
    func,
)
from sqlalchemy.orm import relationship

from coronavirus.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(100), unique=True, nullable=False, comment="用户名")
    password = Column(String(100), nullable=False, comment="密码")
    created_at = Column(DateTime, server_default=func.now(), comment="创建时间")
    book_item = relationship("Book", back_populates="user")

    def __repr__(self):
        return f"{self.username}-{self.password}"


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False, comment="书名")
    address = Column(String(100), nullable=False, comment="地址")
    book_user = relationship("User", back_populates="book")

    def __repr__(self):
        return f"{self.name}-{self.address}"


class City(Base):
    __tablename__ = "city"  # 数据表的表名

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    province = Column(String(100), unique=True, nullable=False, comment="省/直辖市")
    country = Column(String(100), nullable=False, comment="国家")
    country_code = Column(String(100), nullable=False, comment="国家代码")
    country_population = Column(BigInteger, nullable=False, comment="国家人口")
    data = relationship(
        "Data", back_populates="city"
    )  # 'Data'是关联的类名；back_populates来指定反向访问的属性名称

    created_at = Column(DateTime, server_default=func.now(), comment="创建时间")
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间"
    )

    __mapper_args__ = {"order_by": country_code}  # 默认是正序，倒序加上.desc()方法

    def __repr__(self):
        return f"{self.country}_{self.province}"


class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    city_id = Column(
        Integer, ForeignKey("city.id"), comment="所属省/直辖市"
    )  # ForeignKey里的字符串格式不是类名.属性名，而是表名.字段名
    date = Column(Date, nullable=False, comment="数据日期")
    confirmed = Column(BigInteger, default=0, nullable=False, comment="确诊数量")
    deaths = Column(BigInteger, default=0, nullable=False, comment="死亡数量")
    recovered = Column(BigInteger, default=0, nullable=False, comment="痊愈数量")
    city = relationship(
        "City", back_populates="data"
    )  # 'City'是关联的类名；back_populates来指定反向访问的属性名称

    created_at = Column(DateTime, server_default=func.now(), comment="创建时间")
    updated_at = Column(
        DateTime, server_default=func.now(), onupdate=func.now(), comment="更新时间"
    )

    __mapper_args__ = {"order_by": date.desc()}  # 按日期降序排列

    def __repr__(self):
        return f"{repr(self.date)}：确诊{self.confirmed}例"
