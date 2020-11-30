a = 10
while a:
    a -= 1
    print(a)
else:
    print('over')

a = [[1,2,3,4,5],['a','b','c','d']]
for x in a:
    for y in x:
        if y == 2:
            continue #跳过这一步
        elif y == 'c':
            break #强制中断不会执行else语句
        print(y)
    else:
        print('int or str over')
else:
    print('over')

print('for ( i = 0, i < 10, i++) ')
# for ( i = 0, i < 10, i++) 等价于下面的 rang(0,10, 2) 从0开始共取十个数即0-9,2为两个量的距离
for i in range(0, 10, 2):
    print(i, end='|') #end 结尾符，通常为\n
print('--')
for i in range(10, 0, -2):
    print(i, end='|') #end 结尾符，通常为\n

#组织结构
#包=>（子包）=》模块=》类=》函数、变量
#包 dll jar
#文件夹变为包，即添加一个_init_.py文件
#_init_.py文件也是模块，但模块名为包名，即这里的py1
#引用包
print('===')
import day1
print(day1.w)
import test.c as c
print(c.b)

from test.c import b, c,\
    d
# from test.c import (b, c,
#     d)
print(c)

from test import c as cc
print(cc.c)
# from test.c import * #__all__没有d不能导进来  报错

#__init__.py
