from sqlalchemy import Column, Integer, String, Index, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# 连接指定的数据库
engine = create_engine("mysql+pymysql://liu:lh284259@127.0.0.1:3306/python_study?charset=utf8", max_overflow=5)
# 创建一个表需要继承的类
Base = declarative_base()


# 执行原生的sql语句

# cursor = engine.execute('select * from student')
# obj = cursor.fetchall()
# print(obj)

# 使用SQLAlchemy执行orm操作


# 创建单表
class Users(Base):
    __tablename__ = 'test_student'  # 关联表
    id = Column(Integer, primary_key=True, autoincrement=True)  # 创建一列数据
    name = Column(String(16))
    age = Column(Integer)


# Base.metadata.create_all(engine)  # 生成表在表生成之后要注释掉，不然一直会创建这张表
Base.metadata.drop_all(engine)
