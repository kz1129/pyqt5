def hanoi(n, a, b, c):
    if n>0:
        hanoi(n-1, a, c, b)
        print('把%s移到%s \n' %(a, c))
        hanoi(n-1, b, a, c)

hanoi(5, 'A', 'B', 'C')