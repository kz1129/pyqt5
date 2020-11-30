#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
Money = 2000
def AddMoney():
   # 想改正代码就取消以下注释:
   #该方法为局部区域 会访问局部变量 但是找不到 所以要声明是全局
   global Money
   Money = Money + 1
 
print(Money)
AddMoney()
print(Money)

#dir() 函数一个排好序的字符串列表，内容是一个模块里定义过的名字。
import math
print(dir(math))
#特殊字符串变量__name__指向模块的名字，__file__指向该模块的导入文件名。
print(math.__name__, math.__doc__)
# 如果在函数内部调用 locals()，返回的是所有能在该函数里访问的命名。
# 如果在函数内部调用 globals()，返回的是所有在该函数里能访问的全局名字。

Money2 = 2000
def AddMoney2():
   # 想改正代码就取消以下注释:
   #该方法为局部区域 会访问局部变量 但是找不到 所以要声明是全局
   global Money2
   Money = 1
   #两个函数的返回类型都是字典。所以名字们能用 keys() 函数摘取
   print(globals().keys())
   print(locals())
   Money2 = Money2 + 1
 
AddMoney2()

