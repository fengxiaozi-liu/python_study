from orm的增删改查 import models
from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import sessionmaker

engine = create_engine('mysql+pymysql://liu:lh284259@127.0.0.1:3306/flask_study?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()

# 增加操作
# 单个数据的增加
# obj = models.Classes(name='第一班')
# session.add(obj)

# objs = [
#     models.Classes(name='第二班'),
#     models.Classes(name='第三班')
# ]
# # 多个数据的增加
# session.add_all(objs)
# session.commit()

# 查询操作
result = session.query(models.Classes).all()
print(result)

for item in result:
    print(item.id)

# 删除操作
# session.query(models.Classes).filter(models.Classes.id == 1).delete()
# session.commit() # 更改表的数据一定要提交

# 更新操作
# session.query(models.Classes).filter(models.Classes.id==2).update({'name': '第七班'})
# session.query(models.Classes).filter(models.Classes.id == 2).update({models.Classes.name: models.Classes.name + '卡卡西'}
#                                                                     ,synchronize_session=False)
session.query(models.Classes).filter(models.Classes.id==2).update({'name': '第七班'})
session.commit()
session.close()
