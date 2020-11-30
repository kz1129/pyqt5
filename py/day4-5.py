#正则
a = 'py1cpp2pyy3java4php'
print(a.index('cpp')>-1)#T
import re
#re.findall寻找所有符合的子字符串
print(  re.findall('py',a)  ) #'py'普通字符

#数字 \d  非数字\D 
#数字和字符加下划线_ \w  非\W
#\s空白字符  \S非空白字符
print(  re.findall('\d', a)  )# \d = [0-9]  \d 元字符
print(  re.findall('\D', a)  )# \D = [^0-9]

s = 'abc, acd, afc, aef, acf，adc'
m = 'hello1world7good3ddl5file4egg8find9wink6giao1rend'
print(  re.findall('a[df]c', s)  ) #[df] d或者f
print('----')
#[]内为或 [^]即为反义

#数量词{number}
print(  re.findall('[a-z]{3}', m)  )
print('----')
print(  re.findall('[a-z]{3,6}', m)  ) #{3,6}不可加空格成{3, 6}，否则无效

#贪婪，尽可能取范围最大的值，如上面的hel不取取hello
#默认为贪婪，后加?为非贪婪
print(  re.findall('[a-z]{3,6}?', m)  )
# * 0或无限多次
py = 'pytho1python2pythonn'
print('*：匹配包括0在内的任意次数',  re.findall('python*', py) )
# + 1或无限多次
py = 'pytho1python2pythonn'
print('+：匹配不包括0在内的任意次数',  re.findall('python+', py) )
# ? 0或1次，注意跟非贪婪表示不一样，非贪婪的?是在{}后
py = 'pytho1python2pythonn'
print('?：匹配0/1次',  re.findall('python?', py) )

#边界匹配
qq = '1000000000000000001'
print(  '-----',re.findall('^/d{5,10}$', qq)  ) # ^字符串开头 $字符串结尾
print(  re.findall('^000', qq),re.findall('000$', qq)  )

py = 'pythonpythonpythonpython'
nb = 'nbnbnbnbnb'
print(  '多个python/nb',re.findall('(python){3}', py) ,re.findall('nbnbnb', nb)  )

#匹配模式
# . 匹配换行符以外所有字符
language = 'jSC#\nphpcppC#\n'
#匹配模式对应第三个参数 re.I忽略大小写 re.S忽略匹配换行符\n以外所有字符
#此处|为且
print( re.findall('c#.{1}', language, re.I|re.S)  )

#re.sub替换 参数 1被替换 2替换 3目标字符串 4c替换次数 0为默认无数次
print(  re.sub('C#\n', 'css', language, 0)  )
#str.replace() 替换
print(  '--', language.replace('C#\n', 'wxml')  )
print('--', language) #没有改变，需要赋值，如下
language = language.replace('C#\n', 'wxml')
print('--', language)
#sub第二个参数可以为函数，函数返回的数据为替换的新数据
#value为被匹配的字符串信息，多个就有多个信息
language = 'jSC#\nphpcppC#\n'
def convert(value):
    print(value)
    newValue = value.group()#获取被替换的数据
    print('1')
    return 'wxss'+newValue
print(  '函数参数---', re.sub('C#\n', convert, language)  )

ABC = 'ABC456957123EFG8123'
def change(value):
    num = (int)(value.group())
    if num > 6:
        return '9'
    else:
        return '0'
print(  re.sub('\d', change, ABC)  )
#match() 从首字母开始匹配
#search() 搜索 返回结果为对象 需要res.group()取到结果 res.span()返回结果位置
print(  re.match('\d', ABC)  )
print(  re.search('\d', ABC)  )#<re.Match object; span=(3, 4), match='4'>

s = 'python is life'
res  = re.search('python(.*)life', s)
print(res.group(0), '\n括号的字符串', res.group(1)) #group(0)默认输出完整匹配的字符串，1则输出括号内的字符串
print(res.group(0, 1)) 
print(  res.groups()  ) 
#或者这样做
res  = re.findall('python(.*)life', s)
print(res)