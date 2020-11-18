from orm框架 import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

engine = create_engine('mysql+pymysql://liu:lh284259@127.0.0.1:3306/python_study?charset=utf8', max_overflow=5)
Session = sessionmaker(bind=engine)
session = Session()

obj = models.Users(name='alex', age=18)
session.add(obj)
session.commit()
