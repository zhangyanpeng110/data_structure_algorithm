# Author: O98K


"""
    有序列表对于我们的比较是很有用的。在顺序查找中，当我们与第一个项进行比较时，如果
    第一个项不是我们要查找的，则最多还有 n-1 个项目。 二分查找从中间项开始，而不是按
    顺序查找列表。 如果该项是我们正在寻找的项，我们就完成了查找。 如果它不是，我们可以
    使用列表的有序性质来消除剩余项的一半。如果我们正在查找的项大于中间项，就可以消除
    中间项以及比中间项小的一半元素。如果该项在列表中，肯定在大的那半部分。
    然后我们可以用大的半部分重复这个过程。从中间项开始，将其与我们正在寻找的内容进行
    比较。再次，我们找到元素或将列表分成两半，消除可能的搜索空间的另一部分

    这个算法是分而治之策略的一个很好的例子。分和治意味着我们将问题分成更小的部分，以某
    种方式解决更小的部分，然后重新组合整个问题以获得结果

    O(log^n)

    使用切片运算符创建列表的左半部分，然后传递到下一个调用（同样对于右半部分）
    上面做的分析假设切片操作符是恒定时间的。然而，我们知道 Python中的 slice 运算符实际
    上是 O(k)。这意味着使用 slice 的二分查找将不会在严格的对数时间执行。幸运的是，这可以
    通过传递列表连同开始和结束索引来纠正

    即使二分查找通常比顺序查找更好，但重要的是要注意，对于小的 n 值，排序的额外成本可
    能不值得。事实上，我们应该经常考虑采取额外的分类工作是否使搜索获得好处。如果我们
    可以排序一次，然后查找多次，排序的成本就不那么重要。然而，对于大型列表，一次排序
    可能是非常昂贵，从一开始就执行顺序查找可能是最好的选择
"""


# def binarysearch(alist, item):
#     """
#     必须是     有序列表
#     :param alist:
#     :param item:
#     :return:
#     """
#     first = 0
#     last = len(alist) - 1
#     found = False
#
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if alist[midpoint] == item:
#             found = True
#         else:
#             # 往后找
#             if item < alist[midpoint]:
#                 last = midpoint - 1
#             # 往前找
#             else:
#                 first = midpoint + 1
#     return found

# 递归版本
def binarysearch(alist, item):
    """
    必须是     有序列表
    :param alist:
    :param item:
    :return:
    """
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarysearch(alist[:midpoint], item)
            else:
                return binarysearch(alist[midpoint+1:], item)


alist = [20, 21, 22, 25, 30, 55, 80, 91]
print(binarysearch(alist, 50))
print(binarysearch(alist, 30))
