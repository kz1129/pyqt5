import random
def bubble_sort(array):
    for i in range(len(array)-1):
        exchange = False
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                exchange = True
        if not exchange:
            return
        print(array)

li = [random.randint(0, 10000) for i in range(10)]
print(li)
bubble_sort(li)
print(li)

def select_sort(array):
    for i in range(len(array) - 1):
        for j in range(1, len(array) - 1 - i):
            if array[i] > array[j+i]:
                array[i], array[j+i] = array[j+i], array[i]

li2 = [random.randint(0, 100) for i in range(10)]
print(li2)
select_sort(li2)
print(li2)

def insert_sort(array):
    for i in range(1, len(array)):
        tmp = array[i]
        j = i - 1
        while j>=0 and array[j]>tmp:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = tmp

c = [1,5,3,6,8,4,7,9,2]
insert_sort(c)
print(c)




#quick_sort

def partition(array, left, right):
    tmp = array[left] #把左边首个作为标记位
    while left < right:
        while left < right and array[right] >= tmp:
            right -= 1 #右边左移一位
        array[left] = array[right] #往左边移
        while left < right and array[left] <= tmp:
            left += 1
        array[right] = array[left]
    array[left] = tmp
    return left

def quick_sort(array, left, right):
    if left < right:
        mid = partition(array, left, right)
        quick_sort(array, left, mid-1)
        quick_sort(array,mid + 1, right)
d = [1,4,7,2,5,8,3,6,9,10]
quick_sort(d, 0, 9)
print(d)


def sift(array, low, high):
    i = low
    j = 2 * i + 1
    tmp = array[low] #根节点保存下来
    while j <= high:
        if j+1 <= high and array[j] < array[j+1]: # 如果有右孩子，转向右边
            j = j + 1
        if array[j] > tmp:
            array[i] = array[j]
            i = j         # 往下走一层
            j = 2 * i + 1
        else :
            array[i] = tmp #tmp更大
            break
    else:
        array[i] = tmp #把tmp放在叶子节点上

def heap_sort(li):
    n = len(li)
    for i in range((n-2)//2, -1, -1): # 调整时建堆的下标
        sift(li, i, n-1)
    for i in range(n-1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i-1)

li5 = [random.randint(0, 100) for i in range(100)]
print(li5)
heap_sort(li5)
print(li5)

print('归并排序-------------------------')
def merge(Lli, Rli):
    print(Lli,Rli)
    c = []
    h = j = 0
    while j <len(Lli) and h <len(Rli):
        if Lli[j] < Rli[h]:
            c.append(Lli[j])
            j += 1
        else:
            c.append(Rli[h])
            h += 1
    if j == len(Lli):
        for i  in Rli[h:]:
            c.append(i)
    else:
        for i in Lli[j:]:
            c.append(i)
    return c

def merge_sort(li):
    if len(li) <=1:
        return li
    mid = len(li) // 2
    left = merge_sort(li[:mid])
    right = merge_sort(li[mid:])
    return merge(left, right)

li6 = [random.randint(0, 100) for i in range(25)]
print(li6)
li6 = merge_sort(li6)
print('------')
print(li6)
print('*********************************')

def merge2(li,left,right):
    middle= (left+right)//2
    k1 = left
    k2 = middle+1
    k = 0
    newLi=[]
    while k1<=middle and k2<=right:
        
        if li[k1] <= li[k2]:
            newLi.append(li[k1])
            k+=1
            k1+=1
        else:
            
            print(k," ",k2)
            newLi.append(li[k2])
            k+=1
            k2+=1
    
    if k1<=middle:
        for ele in li[k1:middle+1]:
            newLi.append(ele)
    if k2<=right:
        for ele in li[k2:right+1]:
            newLi.append(ele)
    
    for i in range(right-left+1):
        li[i+left] = newLi[i]
    return li

def merge2_sort(li,left,right):
    
    if left<right:
        middle = (left + right)//2
        merge2_sort(li,left,middle)
        merge2_sort(li,middle+1,right)
        return merge2(li,left, right)
    else:
        return li


li6 = [random.randint(0, 100) for i in range(5)]
print(li6)
li = merge2_sort(li6,0,len(li6)-1)
print(li)



