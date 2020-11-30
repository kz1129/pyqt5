x = 1
y = 2
x, y = y, x
print(x)  #2
print(y)  #1
print(type(1 +0.0)) #float
print(type(2/2)) #float
print(type(2//2)) #int
z = 7//3  #取商
w = 7%3   #取余
print(z, w)   #2

0b11 #二进制 >>>模式回车时显示成10进制
0o77 #8进制  同上
0x1D #16进制 同上
print(bin(0b11))  #bin()  转为二进制
print(bin(0o77)) 
print(bin(77)) 

print(int(10))    #int()  转为10进制
print(int(0b10))
print(int(0o10))
print(int(0x10))
                  #oct()  转为8进制 hex转为16进制
#True False首字母大写 type(true)报错
print(bool(1)) #True  0则为False    非0为真  如2 3.0 -5 0b10 0o71 0x4E等
print(int(True)) #1  False则为0
print(bool('')) #False 空字符为False 同样，空数组[]和空对象{} 还有none也为False

#复数  36j

#字符串
print('let\'s go')  # /转义字符
print("let's go")

#回车时用三引号 >>>模式换行可双单引号时直接\
print('''123
123''')
print("""456
12
7\n8""")

#转义字符
print('aa\nbbcc\rdd') 
#输出  aa
#      ddcc    // |r把cc放在行首并替换相应的字符串
# >>> print('aa\nbbbcc\r哈')  //一个中文占两个字符
# aa
# 哈bcc
print('\\n')  #普通字符串
print(r'\\n') #原始字符串 所见即所得

#字符串运算
print('hello'*3) #hellohellohello
print('hello'[1]) #e
print('hello'[-1]) #o
print('hello'[1:3]) #el 即取1-2 1为遇到就开始 3为遇到就结束不取
print('hello'[1:-1]) #el 同上
print('hello'[1:]) #ello  前面的空，则从首开始 都空显示所有