"""
列表中常用的查找方法：顺序查找和二分查找
查找：在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程
列表查找（线性查找）：从列表中查找指定元素
    输入：列表，待查找到的元素
    输出：元素的下标（未找到元素时一遍返回None或者-1）
内置列表查找函数：index（）是用的线性查找
顺序查找
    o(n)
二分查找
    o(logn)

总结：
    二分查找
        首先二分查找一定是有序的列表
        然后我们定义一个左指针，一个右指针
        如果要查找的数比两指针中间的数大，我们就将左指针指向中间
        如果要查找的数比两指针中间的数小，我们将右指针移动到中间
        这样一半一半的去查找我们想查找的数
"""


# 顺序查找
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
        else:
            return None


# 二分查找：二分查找要排序好
def tow_search(li, a):
    length = len(li)
    half = int((length / 2) + 1)
    flag = False
    index = None
    i = 0
    while i < length:
        if a > li[half]:
            half = int((half + length) / 2)
        elif a < li[half]:
            half = int(half / 2)
        elif a == li[half]:
            index = half
            flag = True
            break
        i += 1

    if flag:
        print(f'您想要查找的数{a}在第{index + 1}个位置')
    else:
        print(f'您要想查找的数不存在')


def binary_search(li, val):
    """
    二分查找的函数：二分查找一定是排序好的列表，二分查找的复杂度是o(logn)
    :param li: 传入一个列表
    :param val: 想要查找的值
    :return: 如果能找到值就返回一个下标，找不到就返回none
    """
    left = 0
    right = len(li) - 1
    while left <= right:  # 还有值可以遍历的条件
        mid = (left + right) // 2
        if val < li[mid]:  # 如果想查找的值在左侧就让移动右边的下标
            right = mid - 1
        elif val == li[mid]:  # 如果想找的值和当前的下标相等就返回下标的值
            return mid
        else:  # 如果想查找的值在在右侧就移动左边的下标
            left = mid + 1

    else:
        return None


li = [1, 2, 4, 4, 5, 6, 7, 8, 9]
tow_search(li, 7)
print(binary_search(li, 4))
