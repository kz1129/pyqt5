#嵌套列表-二维数组
print(type(['hello', False, 1, 0.8,{ 'name':'ycy'}, [1, True]])) #<class 'list'>
print(['hello', False, 1, 0.8,{ 'name':'ycy'}, [1, True]][3:5]) # 0.8,{ 'name':'ycy'}
#列表 相加
print(['hello',1,0.8]+['world',0,False]) #['hello',1,0.8,'world',0,False]
#列表乘法
print(['hello', 1]*3) #['hello', 1,'hello', 1,'hello', 1]
#没有减法操作

#元组
print(type( (0, 0.8, 'h', False) )) #<class 'tuple'>
type((1)) 
type(('hh')) ##分别为int 和 str  ()内只有一个元素 纯当作运算
##只有一个元素的表示元组
print(type(   (1,)   )) #<class 'tuple'>
print(type(    ()   ))  #<class 'tuple'>

print((1,2,'3')+(False, [1,2])) #(1, 2, '3', False, [1, 2])
#同样也有乘法 取特定范围值的操作

#str list tuple均为序列 可加乘切片等
print('0123456789'[0:8:2]) #后面的2为所取的字符相差的距离 ，默认为1
print('0123456789'[0:8:1])
#序列的方法
print( 3 in[1,2,3,4,5]) #True 此外还有not in
print('a' not in ('abcndf')) #False
#长度
print(len('abcdef')+len([1,2,3.3,'abcd'])) #6+4=10
#最大最小
print(max( (1, 2, 33, 4) )) #与max( 1,2,33,4 )一样但意义不同
print(min( (2,1,3) )) #1
print(max( 'bcaCE' )) #c>C
# max((1,2,[1,4],3 ))报错
#ord('str') 单个字符转化成asill码


#集合是无序,不重复
print(type( {1,2,3,4,5,6} )) #<class 'set'>
#{1,2,3,4,5}[0] error
#len in not 可用
#求两个集合差值
print( {1,2,3,4,5,5,5,5,5,5}-{1,3} ) #{2,4,5}
#交集
print( {1,3,4,5,6,7,8,9,8,8,8,} & {8})#{8}
#并集
print( {1,3,4,5,6,7,8,9,8,8,8} | {8,11,12} )#{1,3,4,...,8,11,12}
print(type(  set()  ))#定义空集合

#dict 字典 无序
print(type( {} ))#<class 'dict'
print(type(  {1:1,2:3.3,'1':'a',1:2}  )) #tongshang
print( {1:1,2:3.3,'1':1,'1':'a'}['1']  )   #a 相同key取最后那个
#the value of key is can't change and often is int or str or tuple's type

#变量
a = [1,2,3,4,5]
print(a)
#变量命名首字符不能为数字 字母 数字 下划线
#赋值
#id()查看内存
print('赋值')
a = 1
print('a的初始内存' )
print(id(a))
b = a
print('b的初始内存' )
print(id(b))
a = 3
print('a的新内存改变了:' )
print(id(a))
print(b) #1 a改变了b不变

print('-----------')
a = [1,2,3,4,5]
print('a的内存：' )
print(id(a))
b = a
print('b的初始内存' )
print(id(b))
a[0] = 6 #没有指向新的数据
print('a的内存没有改变' )
print(id(a))
print('b的内存没有改变' )
print(id(b))
print(b) #b跟随a改变,但实际上a的指向还是原来的，只是修改其中的值
a = [1,2,3]
print('a的内存改变了' )
print(id(a))
print(b) #此时b没有跟随a改变,因为a的指向变化了
#int str tuple值类型 不可改变(一旦值变了内存也变,即不可以内存不变值改变)
#list set dict 引用类型 可改变如a[0] = 6,即可以内存不变值改变
#字符串不可变示例
# 'python'[0] = o 报错
# 列 元组 list tuple区别
A = [1,2,3]
A[0] = '1'
A.append(4)
print(A) #['1',2,3,4]

print('=========')
#运算
print(5/3) #除,得数是float类型 1.666666666
print(5//2) #不整除,结果2
print(5%2) #取余 得数1
print(2**4) #求幂 得数 2*2*2*2=16
b = 4
b+=b>4 #b>4错误 即b = b + False 无效
print(b) #b=4，b不变
print('----')
print('a'>'b') #比较ascll码
print('abc'> 'acbbb') #false 实际上a相同，即比较第一个不同的字符 list tuple类似
print(True and True) #两者为T才为T
print(True or False) #一个T则为T
print(not True) #F 相反类似 not not True 》True双重否定
print('a' and 'b') #'b'
print('a' or 'b')  #'a'
print( not 'a') #False