#装饰器 
#修改是封闭的，扩展是开放的
import time
def f1():
    print('f1', time.time())
def f2():
    print('f2', time.time())

def printTies(func):
    print('调用了方法')
    func()
printTies(f1)
printTies(f2)
#装饰器做法
print('------装饰器的做法-----')
def decorator(func):
    def wraper():
        print('调用了装饰器方法')
        func()
    return wraper

f = decorator(f1)
f()
m = decorator(f2)
m()
print('-')
print('@decorator-----直接调用，不用改变参数或别的---------------')
def new_decorator(func):
    def wraper():
        print('调用了装饰器方法')
        func()
    return wraper
@new_decorator
def f3():
    print('f3', time.time())
@new_decorator
def f4():
    print('f4', time.time())

f3()
f4()
print('-')
print('@decorator-----一个参数---------------')
def new_decorator(func):
    def wraper(func_dec):
        print('调用了装饰器方法')
        func(func_dec)
    return wraper
@new_decorator
def f3(func_name_f3):
    print('f3', time.time(), func_name_f3)

f3('f3加一个参数')

print('-')
print('@decorator-----多个参数---------------')
def new_decorator(func):
    def wraper(*args, **kw):
        print('调用了装饰器方法')
        func(*args, **kw)
    return wraper
@new_decorator
def f5(func_name_f5):
    print('f5', time.time(), func_name_f5)
@new_decorator
def f6(func_name_f6, func_name_f6_2):
    print('f6', time.time(), func_name_f6, func_name_f6_2)
@new_decorator
def f7(func_name_f7, func_name_f7_2, **kw):
    print('f7', time.time(), func_name_f7, func_name_f7_2)
    print(kw)

f5('f5加一个参数')
f6('f6加两个参数', '第二个参数')
f7('1','2',a = 1, b = 2, c = 'cc')