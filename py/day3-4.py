#test inti.py已经导入了
# import sys
# import datetime
# import io
# 直接导入test即可
import test

sys.setrecursionlimit(1000000) #循环次数限制

print(sys.path)

#循环引入一直import
#p1.py
# from p2 import p2
# p1 = 2

# p2.py
# from p1 import p1
# p2 = 1
a = 1.123456
result = round(a, 2) #2为保留的小数,会自动4舍5入
print(result)

#函数 没有return返回none
def calculation(x, y):#形参
    return x+y, x-y #返回元组
def noresult():
    print('uuu')

result1, result2 = calculation(3,4) #序列解包 实参
print(calculation(3,4),result1, result2, noresult()) #(7, -1) 7 -1 None

#序列解包
a, b, c = 1, 2, 3
d = 1, 2, 3
print(type(d))
e, f, g = d
h = [1, 2, 3]
i, j, k = h
print(i,j,k) 

result3 = calculation(y=5, x=1) #关键字参数
#默认参数
def add(x, y=1):
    return x+y
print(add(1)) #只传x

#相同的参数，先全局后局部

#类
class Student():
    #类变量
    sum = 0
    totalAge = 0 #平均年龄
    __name = ''
    age = 0
    def __init__ (self, name, age):
        #实例变量
        #name = name 不会改变实例的name，age
        self.__name  = name
        self.age = age
        print('----',self.__name, self.age)###访问的是实例变量
        print('----',name, age)###访问的是形式变量
        sum = 1
        print('===',sum) #调用的是方法内新建的sum，跟条件语句不一样，条件语句调用的是全局再局部
        #构造函数 实例化即调用 无return否则报错
        #访问类变量两种方法
        Student.sum += 1
        self.__class__.totalAge += age
        print('学生总数',Student.sum)
        print('学生总年龄', self.__class__.totalAge)
    def setName(self, str):
        self.__name = str
    def getName():
        return __name
    def showInfo(self):#self必加 跟this差不多
        print('年龄', self.age, '姓名', self.__name)
    #类方法，计算平均年龄
    @classmethod
    def AverageAge(cls):
        print('平均年龄',cls.totalAge/cls.sum)
    #静态方法，没有强制要求参数,对象和类均可调用
    @staticmethod
    def add(x, y):
        pass


class Teacher():
    name='类变量'
    def __init__(self, name):
        name = name#没有给实例变量赋值

student1 = Student('kza', 10)  #学生总数1
student1.setName('newkza')
# student1.name = 'newkza' 公开变量可以用，但不建议，而阻止这种设置则将变量变为私有__变量名 如 __name
print('newName', student1.getName())
student3 = Student('ka',11)    #学生总数2
Student.AverageAge()#调用类方法，也可以直接拿对象去调用student1.AverageAge()但建议不用
print('--------------------------')

student2 = student1
student1.showInfo()#类外调用 可类内调用
print(student1.__dict__)#实例所有的变量

teacher1 = Teacher('实例变量')
print(teacher1.__dict__)#实例所有的变量,为空
#实例变量没有，然后寻找类变量(还是没有找到则在父类中寻找)，最终name='类变量'
print(teacher1.name)

print(id(student1),id(student2)) #相同
print('----------------------------')

