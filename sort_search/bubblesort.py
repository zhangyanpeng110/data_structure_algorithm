# Author: O98K

"""
冒泡排序
    需要多次遍历列表。它比较相邻的项并交换那些无序的项
    *****每次遍历列表将下一个最大的值放在其正确的位置
    实质上，每个项“冒泡”到它所属的位置

    1.每完成一次内层循环，都会将最大的数冒泡到最上面(索引最大的位置)
    2.每完成一次内层循环，每次循环都使得右 边 的数肯定 大于 左边 的数

    O(n^2)
"""


def bubblesort(alist):
    for i in range(1, len(alist)):
        # 0 => 0,1  1 => 0,2 2 => 0,3
        for j in range(i + 1):
            if alist[i] < alist[j]:
                alist[i], alist[j] = alist[j], alist[i]


alist = [32, 10, 65, 1, 5, 103, 48, 62, 44, 64]
bubblesort(alist)
print(alist)

"""
短冒泡排序：
    如果发现列表已排序，可以修改冒泡排序提前停止
    这意味着对于只需要遍历几次列表，冒泡排序具有识别排序列表和停止的优点
"""


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                exchanges = True
                alist[i + 1], alist[i] = alist[i], alist[i + 1]
        passnum = passnum - 1


alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
shortBubbleSort(alist)
print(alist)
