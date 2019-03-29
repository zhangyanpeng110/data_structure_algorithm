# Author: O98K


"""
选择排序：
    选择排序改进了冒泡排序，每次遍历列表只做一次交换。为了做到这一点，一个选择排序在
    他遍历时寻找最大的值，并在完成遍历后，将其放置在正确的位置。与冒泡排序一样，在第
    一次遍历后，最大的项在正确的地方。 第二遍后，下一个最大的就位。遍历 n-1 次排序 n 个
    项，因为最终项必须在第（n-1）次遍历之后

    O(n^2 )
"""


def selectionsort(alist):
    length = len(alist)
    for i in range(length-1, 0, -1):
        index = 0
        for j in range(1, i+1):
            if alist[j] > alist[index]:
                index = j
        alist[i], alist[index] = alist[index], alist[i]


alist = [20, 21, 22, 25, 56, 30, 55, 80, 61]
selectionsort(alist)
print(alist)
