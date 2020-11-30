# from urllib import request
import requests
import re
import time

class Spider():
    badeUrl = 'https://space.bilibili.com/2790716/video?page='
    def __fetch_content(self):#私有方法

        for i in range(1):
            page = str(i+1)
            url = Spider.badeUrl + page
            r = requests.get(url)
            print(r.text)
            
        # r = requests.get(Spider.url)
        # print(type(r.text))
        # res = re.sub('</span><span>.*class=\"title\"', '', r.text)
        # print(type(res))
        # res1 = re.findall('class=\"title\">(.*)</a><!---->', res)
        # i = 1

        # path = 'C:\\Users\\kongs\\Desktop\\用户泰然自若.txt'
        # fo = open(path, 'a',encoding='utf-8')
        # localtime = time.asctime( time.localtime(time.time()) )
        # fo.write(localtime + '\n')
        # for v in res1:
        #     w = str(i) +':'+ v + '\n'
        #     fo.write(w)
        #     i += 1
        # print('写入成功！')
        # fo.close()
    def go(self):
        self.__fetch_content()

spider = Spider()
spider.go()