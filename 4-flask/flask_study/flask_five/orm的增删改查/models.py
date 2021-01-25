from sqlalchemy import Column, Integer, String, Index, UniqueConstraint, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
import datetime

# 连接指定的数据库
engine = create_engine("mysql+pymysql://liu:lh284259@127.0.0.1:3306/flask_study?charset=utf8", max_overflow=5)
# 创建一个表需要继承的类
Base = declarative_base()


class Classes(Base):
    __tablename__ = 'class'  # 关联表
    id = Column(Integer, primary_key=True, autoincrement=True)  # 创建一列数据
    name = Column(String(16), unique=True, nullable=False)


class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True, autoincrement=True)  # 创建一列数据
    name = Column(String(16), unique=True, nullable=False)
    password = Column(String(32), nullable=False)
    ctime = Column(DateTime, default=datetime.datetime.now)
    cls_id = Column(Integer, ForeignKey('class.id'))
    # 增加这条数据之后不会在数据库中增加字段，只会帮忙主动做联表操作
    cls = relationship('Classes', backref='status')


class Hobby(Base):
    __tablename__ = 'hobby'
    id = Column(Integer, primary_key=True, autoincrement=True)
    caption = Column(String(32), default='篮球')


class StudentToHobby(Base):
    __tablename__ = 'studnettohobby'
    id = Column(Integer, primary_key=True, autoincrement=True)
    student_id = Column(Integer, ForeignKey('student.id'))
    hobby_id = Column(Integer, ForeignKey('hobby.id'))

    # 创建一个联合唯一索引
    # __table_args__ = (
    #     UniqueConstraint('student_id', 'hobby_id', name='uix')
    # )


Base.metadata.create_all(engine)
