#topk问题 冒泡
import random
def topk(list, k):
    topk = []
    l = len(list)
    while k>0:
        for i in range(l-1):
            if li1[i] > li1[i+1]:
                li1[i], li1[i+1] = li1[i+1], li1[i]
        topk.append(li1[l-1])
        l -= 1
        k -= 1
    return topk

li1 = [random.randint(0, 100) for i in range(25)]
print(li1)
topk = topk(li1, 5)
print(topk)

print('----------shell sort----------------')
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        tmp = li[i] 
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j+gap] = li[j]
            j -= gap
        li[j + gap] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d = d //2

li = list(range(25))
import random
random.shuffle(li)
print(li)
shell_sort(li)
print(li)