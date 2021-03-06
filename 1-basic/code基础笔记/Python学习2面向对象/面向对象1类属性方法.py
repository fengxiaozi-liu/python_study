"""
基本理论
    什么是对象
        万物皆可对象
        对象包含属性（名词）和行为(动词)
        对象的里面才有属性和行为
    Python中的体现
        Python是一门特别彻底的面向对象（oop）的编程对的语言
        Python全部数据归结为对象数据类型
    面向过程和面向对象
        面向过程：解决问题的每一个过程和每一个步骤
        面向对象：在解决问题的过程中给解决问题所需要的对象
    对比
       面向对象是面向过程的封装（要采取一定的措施只要调用相应的对象就好了）
       面向过程重要的是（1.按照步骤划分，2.把一个任务分解成多个步骤）
       面向对象重要的是（1按照对象进行划分2确定对象的属性和行为）
    面向过程转换为面向对象编程思想
        1列举出每一个任务的具体实现步骤
        2试图分离这些实现步骤中的代码块
        3将这些代码模块划分到某一个对象中
        4根据这个对象的属性和行为，抽象出对应的类 设计类
什么是类
    作用
        根据抽象的类产生具体的对象
    类的构成
       类由名称 属性 和 方法构成
       注意：1.类的属性和方法是抽象的概念
            2.在产生对象之后，对象才拥有具体的属性值和方法实现
如何定义一个类
    class 类名:
        对应的描述(函数的体代码)
类的注意事项：
    经典类 和 新式类
    命名规范符合大驼峰原则
通过类创建一个对象
    对象名 = 类名()
属性相关
    属性和变量的区别
        1变量是可以改变的量值
        2属性是数以某个对象的特性
        3变量有全局变量哥局域变量可以根据不同的位置存在不同权限的访问
        4属性只能对对象进行访问
        5对象是通过变量名进行引用的，而既然是变量就有相对应的访问
        6属性与变量的判断依据是是否存在宿主
    对象属性
        创建对象的属性1直接通过对象，动态添加
                   2通过类的初始化方法进行创建 对象名.想要添加的属性 = 赋值
        访问对象的属性
            变量存储着数据的地址
            访问对象是通过访问相关变量的地址栏
            对象.__dict__ 访问对象全部的属性 以字典的形式打印出来
        删除对象的属性
            del 对象名.变量名
    类属性
        根据同一类创建的不同对象之间不能互相访问（一个对象中的属性不能访问其他对象中的属性）
        创建类属性
            1类名.对象 = 数据(将类看成一个对象)
            2class 类名：(通过类添加属性)
                增加想要的属性
        访问类属性
            类名.__dict__(访问类的全部对象)
            对象名.类中的属性名（通过对象进行访问） 对象先在自己身上找属性找到就会停止寻找如果没有就去类上面去寻找
        修改类属性
            类名.属性 = 数据（通过类名进行修改）
        删除类属性
            del 类名.属性名
        注意：
            1类属性的内存存储
                类对象里面的dict只读不能修改
            2对象的内存存储
                对象名.__dict__ ={key:value}
                对象中的dict可以修改，通过dict也可以修改对象中的相关属性
            3类属性被各个对象共享
    对象属性和类属性的区别和联系
    高级--限制属性的添加
        class 类名：
            __slots__ = [只能添加的属性]
        通过slots添加限制属性只能添加列表里面的属性
"""


# 测试创建类（如何定义一个类）
# class Money:
# 根据这个创建一个对象（实例化）
# print(Money.__name__)
# 创建对象属性
# 1创建一个类经典类 和 新式类
class Person:
    pass


# 2 根据这个类创建一个对象
p1 = Person()
p2 = Person()
# 3根据类增加一个属性
p1.age = 18
p1.height = 180
# 验证属性是否添加成功
print(p1.age)
# 查看所有的属性
print(p1.__dict__)
print(Person.__dict__)
p2.address = '上海'
# 测试增加类属性
Person.money = '人命币'
print(Person.money)


# 通过类创建类属性
class Person:
    age = 5
    name = 'xiaoming'
    height = 180


# 访问类属性1
print(Person.__dict__)
# 通过类的对象访问类属性
p3 = Person()
print(p3.name)
print(p3.age)
Person.age = 6
print(Person.__dict__)
# 测试对象的内存存储
p3.__dict__ = {'name': 'xiaohong', 'heiget': 180}
p3.weight = 60
print(p3.__dict__)
# 测试类dict的只读属性
# Person.__dict__ = {'name':'xiaohong'}
# Person.__dict__['name'] = 'xiaohong'
# 测试类的属性共享
p4 = Person()
print(p4.age)
# 测试属性的可变性
p3.age += 5
print(p3.age)
print(Person.age)
