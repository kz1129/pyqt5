def curve_pre():
    print(1)
    a = 10
    def curve(x):
        print(2)
        return a*x*x
    return curve
#闭包 函数+环境变量 不受外部影响
# curve()报错
a = 1 #不调用
f = curve_pre() #没有调用curve
print('-')
s1 = f(5) #调用curve
print('等价于')
s2 = curve_pre()(5)
print(s1, s2)
print('--',f.__closure__)
print('--',f.__closure__[0].cell_contents)

def f1():
    b = 10
    def f2():
        b = 20 #b为局部变量 不会影响外面 没有用到外面场景的环境变量不是闭包
        print('f2',b)
    print('f1',b)
    print(f2.__closure__)
    print(b)
f1()
print('对比----------')
def f1():
    b = 10
    def f2():
        # b = 20 #b为局部变量 不会影响外面 不是闭包
        print('f2',b)
    print('f1',b)
    print(f2.__closure__)
    print(b)
f1()

print('--')
print('--')
origin = 0
def go(step):
    # new_step = origin + origin
    # # origin = new_step 报错，因为这里把origin变为局部变量，上一行找不到
    global origin
    new_step = origin + step
    origin = new_step
    return origin

def first(pos):
    def second(step):
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return second

        
tourist = first(origin)
#tourist会保持pos的变化的值，origin不变，保持为0
print(tourist(3), origin)
print(tourist(2), origin)
print(tourist(5), origin)