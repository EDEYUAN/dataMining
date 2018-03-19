# _*_ coding:utf-8 _*_
# __Author:edeyuan
# Version: 1.0
# Time:2018/03/17


from bs4 import BeautifulSoup
import urllib2
import json
import sys


def loadrequest(number, items):
    headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"}
    req = urllib2.Request('https://hr.tencent.com/position.php?start=' + str(number), headers=headers)
    html = urllib2.urlopen(req).read()

def phase(html, items):
    soup = BeautifulSoup(html, 'lxml')  # BeautifulSoup是一个网页解析库
    odd = soup.select('.odd')
    even = soup.select('.even')

    whole = odd + even
    for item in whole:
        _item = {}
        _item['positionName'] = item.select('td')[1].get_text()
        _item['positionLink'] = 'http://hr.tencent.com' + item.select('td a')[0].attrs['href']
        _item['positionType'] = item.select('td')[1].get_text()
        _item['positionPlace'] =item.select('td')[2].get_text()








if __name__ == '__main__':
    number = 0
    items = []
    switch = True
    while switch:
        if number >= 50:
            # 爬50页,这个相当于一个开关,如果请求发出,爬虫就启动
            switch = False
        loadrequest(number, items)
        # 一次性爬取10页数据
        number += 10
    content = json.dumps(items, ensure_ascii=False)
    with open('zhaoping.json', 'w') as f:
        f.write(content)







