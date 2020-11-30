#requsets模块
# requests.get(params[]) params : url header
import requests
url1 = 'http://localhost/ThinkPHP5.07/index.php/api/v1/newsItem/3'
headers1 = {'User-Agent':'AJEST'}
res1 = requests.get(url = url1, headers = headers1)
print(res1.request.headers) #注意这里的request没有s


url2 = 'localhost/ThinkPHP5.07/poc_test/requests_timeout.php'
try:
    res2 = requests.get(url =url2, timeout=4)
    print(res2.text)
except Exception as e:
    print('timeout')

url3 = 'http://localhost/ThinkPHP5.07/poc_test/requests_getparams.php'
#构造get参数
getparams = {'news_id':3, 'cat_id':1}
res3 = requests.get(url = url3, params = getparams)
print(res3.text)


#文件上传

#总结 requests 重要的模块
#  1定制头部headers User-Agent
#  2定制超时时间
#  3构造get-params  post-data传参

