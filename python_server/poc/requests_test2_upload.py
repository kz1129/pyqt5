import requests
url = 'http://localhost/ThinkPHP5.07/poc_test/upload.php'
uploadfile = {'filename':open(r'D:/files/大三/毕设_相关/python_server/poc/test.txt', 'rb')}
postData = {'submit':'提交'}

res = requests.post(url = url, files = uploadfile, data = postData)
print(res.text)


# 上传文件 
#  cookie 提交 res = requests.post(url = url, cookie=coo)
