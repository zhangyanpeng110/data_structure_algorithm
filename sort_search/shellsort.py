# Author: O98K


"""
希尔排序：
    有时称为“递减递增排序”，通过将原始列表分解为多个较小的子列表来改进插入排
    序，每个子列表使用插入排序进行排序。 选择这些子列表的方式是希尔排序的关键。不是将
    列表拆分为连续项的子列表，希尔排序使用增量i（有时称为 gap ） ，通过选择 i 个项的所有
    项来创建子列表


    乍一看，你可能认为希尔排序不会比插入排序更好，因为它最后一步执行了完整的插入排
    序。 然而，结果是，该最终插入排序不需要进行非常多的比较（或移位） ，因为如上所述，
    该列表已经被较早的增量插入排序预排序。 换句话说，每个遍历产生比前一个“更有序”的列
    表。 这使得最终遍历非常有效

    它倾向于落在 O(n) 和O(n^2 ) 之间的某处，基于以上所描述的行为。对于 Listing 5中显示的增量
    性能为 O(n^2 )

    通过改变增量，例如使用 2^k -1（1,3,7,15,31等等） ，希尔排序可以在 O（n^3/2 ） 处执
    行
"""


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount,
              "The list is", alist)
        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentvalue


alist = [54, 26, 93, 17, 77, 44, 55, 20]
shellSort(alist)
print(alist)

# 平均分   四舍五入取组数
# count = len(alist) // 2
# print(count)



