

"""冒泡排序
比较相邻的元素。如果第一个比第二个大，就交换他们两个。
对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
针对所有的元素重复以上的步骤，除了最后一个。
持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。
以上节选自维基百科
"""
def bubble_sort(numberlist):
    length = len(numberlist)
    for i in range(length):
        for j in range(1,length-i):
            if numberlist[j-1] > numberlist[j]:
                numberlist[j],numberlist[j-1] = numberlist[j-1],numberlist[j]
    return numberlist

"""选择排序
选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。
首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
"""

def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1,len(arr)):
        if smallest > arr[i]
        smallest_index = i
    return smallest_index

def selectSort(arr):
    newArr = []
    while arr:
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


"""插入排序
从第一个元素开始，该元素可以认为已经被排序
取出下一个元素，在已经排序的元素序列中从后向前扫描
如果该元素（已排序）大于新元素，将该元素移到下一位置
重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
将新元素插入到该位置后
重复步骤2~5
"""
def insert_sort(data):
    for k in range(1, len(data)):
        cur = data[k]
        j = k
        while j > 0 and data[j - 1] > cur:
            data[j] = data[j - 1]
            j -= 1
        data[j] = cur
    return data


"""希尔排序
希尔排序通过将比较的全部元素分为几个区域来提升插入排序的性能。
这样可以让一个元素可以一次性地朝最终位置前进一大步。然后算法再取越来越小的步长进行排序，
算法的最后一步就是普通的插入排序，但是到了这步，需排序的数据几乎是已排好的了（此时插入排序较快）
"""
def shell_sort(numberlist):
    length = len(numberlist)
    gap = length // 2
    while gap > 0:
        for i in range(gap, length):
            temp = numberlist[i]
            j = i
            while j >= gap and numberlist[j - gap] > temp:
                numberlist[j] = numberlist[j - gap]
                j -= gap
            numberlist[j] = temp
        gap = gap // 2
    return numberlist

"""归并排序
原理如下（假设序列共有{displaystyle n}个元素）：
将序列每相邻两个数字进行归并操作，形成{displaystyle ceil(n/2)}个序列，排序后每个序列包含两/一个元素
若此时序列数不是1个则将上述序列再次归并，形成{displaystyle ceil(n/4)}个序列，每个序列包含四/三个元素
重复步骤2，直到所有元素排序完毕，即序列数为1
"""
def  merge(left, right):
    result = []
    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

def merge_sort(numberlist):
    if len(numberlist) <= 1:
        return numberlist
    mid = len(numberlist) // 2
    left = numberlist[:mid]
    right = numberlist[mid:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


"""快速排序
从数列中挑出一个元素，称为“基准”（pivot），
重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。
在这个分割结束之后，该基准就处于数列的中间位置。这个称为分割（partition）操作。
递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，
它至少会把一个元素摆到它最后的位置去。科
"""
def quick_sort(array):
        if len(array) < 2:
            return array
        else:
            pivot = array[0]
            less = [i for i in array[1:] if i <= pivot]
            greater = [i for i in array[1:] if i > pivot]
            return quick_sort(less) + [pivot] + quick_sort(greater)


"""堆排序
若以升序排序说明，把数组转换成最大堆积(Max-Heap Heap)，这是一种满足最大堆积性质(Max-Heap Property)的二叉树：对于除了根之外的每个节点i, A[parent(i)] ≥ A[i]。

重复从最大堆积取出数值最大的结点(把根结点和最后一个结点交换，把交换后的最后一个结点移出堆)，并让残余的堆积维持最大堆积性质。
"""
def heap_sort(numberlist):
    length = len(numberlist)
    def sift_down(start, end):
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and numberlist[child] < numberlist[child + 1]:
                child += 1
            if numberlist[root] < numberlist[child]:
                numberlist[root], numberlist[child] = numberlist[child], numberlist[root]
                root = child
            else:
                break

# 创建最大堆
    for start in range((length - 2) // 2, -1, -1):
        sift_down(start, length - 1)

# 堆排序
    for end in range(length - 1, 0, -1):
        numberlist[0], numberlist[end] = numberlist[end], numberlist[0]
        sift_down(0, end - 1)

    return numberlist


"""计数排序
def counting_sort(numberlist, maxnumber):  # maxnumber为数组中的最大值
    length = len(numberlist)  # 待排序数组长度
    b = [0 for i in range(length)] # 设置输出序列，初始化为0
    c = [0 for i in range(maxnumber+ 1)]  # 设置技术序列，初始化为0
    for j in numberlist:
        c[j] = c[j] + 1
    for i in range(1, len(c)):
        c[i] = c[i] + c[i - 1]
    for j in numberlist:
        b[c[j] - 1] = j
        c[j] = c[j] - 1
    return b
"""