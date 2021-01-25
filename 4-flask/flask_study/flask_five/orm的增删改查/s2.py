from sqlalchemy import text

from orm的增删改查 import models
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import create_engine

engine = create_engine('mysql+pymysql://liu:lh284259@127.0.0.1:3306/flask_study?charset=utf8')

Session = sessionmaker(bind=engine)
session = Session()

# 关于SQLAlchemy的查询操作
result = session.query(models.Classes).all()
result2 = session.query(models.Classes.id, models.Classes.name).all()
result1 = session.query(models.Classes.id, models.Classes.name).filter(models.Classes.id == 3).first()
result3 = session.query(models.Classes.id, models.Classes.name).filter_by(id=3).first()
result4 = session.query(models.Classes).filter(text('id =:value or name=:name')).params(
    value=2,
    name='第三班').order_by(models.Classes.id).all()

# 联表查询
# student_list = [
#     models.Student(name='张三', password='123', cls_id=2),
#     models.Student(name='李四', password='456', cls_id=3),
# ]
# session.add_all(student_list)
# session.commit()
objs = session.query(models.Student.id, models.Student.name, models.Classes.name).join(models.Classes,
                                                                                       isouter=True).all()
print(objs)

print(result)
print(result1)
print(result2)
print(result3)
for item in result4:
    print(item.id, item.name)

objs2 = session.query(models.Student).all()
for item in objs2:
    print(item.id, item.name, item.cls.name)

obj3 = session.query(models.Classes).filter(models.Classes.name == '第七班').first()
for item in obj3.status:
    print(item.id, item.name)

session.close()
