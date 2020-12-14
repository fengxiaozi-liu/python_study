# 冒泡排序
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                exchange = True
                li[j], li[j + 1] = li[j + 1], li[j]
        if not exchange:
            break
    return li


# 选择排序：假定认为无序区最左边的数为最小值，如果出现比这个值还小的就交换这两个值
def select_sort(li):
    for i in range(len(li) - 1):
        min_num = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_num]:
                min_num = j
        li[i], li[min_num] = li[min_num], li[i]
    return li


# 插入排序：在无序区随机选择一张牌，如果出现的这个牌比指针所指向的牌的数小，我们就让它插入进来
def insert_sort(li):
    for i in range(1, len(li)):
        temp = li[i]
        j = i - 1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp
    return li


# 快速排序：快速排序又叫做二分排序，是通过将最左边的数进行归位，然后迭代完成
def partition(li, left, right):
    temp = li[left]
    while left < right:
        while left < right and li[right] >= temp:
            right -= 1
        li[left] = li[right]
        while left < right and li[left] <= temp:
            left += 1
        li[right] = li[left]
    li[left] = temp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)
    return li


li = [3, 5, 2, 6, 4, 7, 9]
la = [3, 5, 2, 6, 4, 7, 9]
lb = [3, 5, 2, 6, 4, 7, 9]
lc = [5, 7, 4, 6, 3, 8, 22, 1, 2, 10, 9, 8]
print(bubble_sort(li))
print(select_sort(la))
print(insert_sort(lb))
print(quick_sort(lc, 0, len(lc)-1))
