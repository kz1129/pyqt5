#JSON vs xml
#javascript Object Notation 对象标记 轻量级的数据交换格式
#跨语言
#dict格式
# {
#     'name':'kza'
# }
#反序列化 字符串=>json数据
import json
json_str ='{"name": "kza", "age":18 }' #里面必须为双引号，固定格式
# json.loads() str转为json数据
student = json.loads(json_str)
print(type(student), student)
json_str ='[{"name": "kza", "age":18 },{"name": "kzaq", "age":19 }]'
student = json.loads(json_str)
print(type(student), student)
#序列化
student_str = json.dumps(student)
print('==',type(student_str),student_str)