import requests
import re
url = 'http://54.168.43.75:17777/l4/'

res = requests.get(url = url).text.replace(' ','')
res1 = re.findall(r'-?\d+', res)
a, b, u, n = int(res1[3]), int(res1[4]), int(res1[6]),  int(res1[7])
res2 =re.findall('U<sub>n</sub>]([-+])', res)[0]


if res2 == '-':
    for i in range(n):
        u = a + u - i*b
else:
    for i in range(n):
        u = a + u + i*b


url = 'http://54.168.43.75:17777/l4/1.php' 
getparams = {'result':u}
print(getparams)
res3 = requests.get( url= url, params=getparams)
print(res3.text)