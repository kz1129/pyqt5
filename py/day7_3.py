# from urllib import request
import requests
import re
import time

class Spider():
    url = 'http://www.bilibili.com/ranking/all/0/0/3'
    def __fetch_content(self):#私有方法
        # r = request.urlopen(Spider.url)
        # html = r.read()
        # html = str(html, encoding='utf-8')#编码
        # print(html)s
        r = requests.get(Spider.url)
        print(type(r.text))
        res = re.sub('</span><span>.*class=\"title\"', '', r.text)
        print(type(res))
        res1 = re.findall('class=\"title\">(.*)</a><!---->', res)
        i = 1

        path = 'C:\\Users\\kongs\\Desktop\\b站排行榜.txt'
        fo = open(path, 'a')
        localtime = time.asctime( time.localtime(time.time()) )
        fo.write(localtime)
        for v in res1:
            w = str(i) +':'+ v + '\n'
            fo.write(w)
            i += 1

    def go(self):
        self.__fetch_content()

spider = Spider()
spider.go()