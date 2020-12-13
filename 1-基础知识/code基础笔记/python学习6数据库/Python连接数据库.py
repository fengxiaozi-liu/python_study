import pymysql

# host是服务器的主机地址
# user是连接数据库的用户
# password是数据库的密码
# 打开一个数据库的连接获取一个db对象
db = pymysql.connect(host='localhost', user='root', password='Lh284259@', database='python201', port=3306,
                     charset='utf8')
# 获取到cursor游标对象
cursor = db.cursor()
cursor.execute('select * from student')
db.commit()
print(cursor.fetchone())

db.close()
