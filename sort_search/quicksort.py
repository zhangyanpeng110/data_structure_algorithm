# Author: O98K

"""
快速排序首先选择一个值，该值称为 枢轴值 。虽然有很多不同的方法来选择枢轴值，我们将
使用列表中的第一项。枢轴值的作用是帮助拆分列表。枢轴值属于最终排序列表（通常称为
拆分点） 的实际位置，将用于将列表划分为快速排序的后续调用


"""
def quicksort(alist):
    length = len(alist)
    if length < 2:
        return alist
    else:
        currentvalue = alist[0]
        left_list = [value for value in alist if value < currentvalue]
        right_list = [value for value in alist if value > currentvalue]
    return quicksort(left_list) + [currentvalue] + quicksort(right_list)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quicksort(alist)
print(quicksort(alist))
"""

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
    
def quickSortHelper(alist,first,last):
    if first<last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
        
def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first+1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        
        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
            
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
"""
