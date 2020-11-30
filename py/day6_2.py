#枚举 不可变 不可重复
from enum import Enum 
class VIP(Enum):
    YELLOW = 1
    GREAN = 2
    RED = 3
    huangse = 1
    BLUE = 8
print(VIP.RED,VIP['GREAN'],type(VIP.RED))#VIP.RED enum
print(VIP.RED.name, type(VIP.RED.name)) #str
#字典和类表示  缺陷：可变，不能排除重复
#a = {'YELLOW':1, 'GREAN':2}
# class typeDiamond:
#     YELLOW = 1
#     GREAN = 2
#可变 a['YELLOW'] = 4                       # s = (1,2,3)
#typeDiamond.YELLOW = 5                     # s[0] = 4
#VIP.YELLOW = 6    报错                     # print(s)

#比较
print(VIP.GREAN == VIP['GREAN'])
#别名
print(VIP.huangse) #VIP.YELLOW
for v in VIP:#别名不打印
    print('循环---',v, type(v))
for v in VIP.__members__:#别名打印
    print('打印别名---',v, type(v))
for v in VIP.__members__.items():#别名打印
    print('打印别名项---',v, type(v))

#转换
print(VIP(8)) #实际上不是int()之类的转换
from enum import IntEnum, unique
#unique避免枚举重复
@unique
class color(IntEnum):
    BLACK = 1
    # GREY = 1
    WHITE = '2'
    # GREAT = 'sh'