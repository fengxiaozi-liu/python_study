"""
元组：如果想要存储多个数据，但是这些数据是不能修改的
    列入：身份证号是不能修改的
定义元组
    元组特点：定义元组使用小括号（即使只有一个数据也要加逗号如果没有逗号则数据是什么类型他便是什么类型），且逗号隔开各个数据
    数据可以使不同的数据类型
元组的查找数据：
    元组名.[下标] 查找指定下标的数据
    元组名.index(数据) 返回指定数据的下标
    元组名.count(数据) 返回数据在元组中出现的次数
    len(元组名) 返回元组的长度
元组的修改操作
    元组里面嵌套了列表 列表中的数据仍然支持修改
"""
# 测试元组的修改
t1 = ('aa', 'bb', 'cc', 'dd')
t2 = ('aa', 'bb', ['cc', 'dd'])
# 元组中列表的修改
# t2[2][0] = 'xiaoming'
# print(t2[2][0])

list1 = [1, 2, 3, 4]
list2 = [2, 3, 4]
list3 = list1 + list2
print(id(list1))
print(id(list2))
print(id(list3))
print(list3)