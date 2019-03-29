# Author: O98K


"""
短冒泡排序：
    如果发现列表已排序，可以修改冒泡排序提前停止
    这意味着对于只需要遍历几次列表，冒泡排序具有识别排序列表和停止的优点

    O(n^2 )
"""


def shortbubblesort(alist):
    sort_flag = True

    length = len(alist)
    while length > 0 and sort_flag:
        sort_flag = False
        for i in range(length-1):
            if alist[i] > alist[i + 1]:
                sort_flag = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        length -= 1
    return alist


alist = [20, 21, 22, 25, 56, 30, 55, 80, 61]
shortbubblesort(alist)
print(alist)
