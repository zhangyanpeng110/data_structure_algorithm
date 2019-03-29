# Author: O98K


"""
插入排序：
    insertSort（ActiveCode 1）的实现展示了存在n-1个遍历以对n个排序
    从位置 1开始迭代并移动位置到 n-1，因为这些是需要插回到排序子列表中的项

    O(n^2 )
"""


def insertionsort(alist):
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        # 每次 while 都使得当前值 大于 左边的值
        while position > 0 and alist[position-1] > currentvalue:
            alist[position] = alist[position-1]
            position -= 1

        alist[position] = currentvalue


alist = [32, 10, 65, 1, 5, 103, 48, 62, 44, 64]
insertionsort(alist)
print(alist)
