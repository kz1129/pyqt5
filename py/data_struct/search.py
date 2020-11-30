a = [1, 4, 5, 6, 77, 9, 3, 12, 20]

def linear_search(array, x):
    l = len(array)
    for i in range(l):
        if array[i] == x:
            print('在%s位' %(i))
            return
    print('not found')

linear_search(a, 6)