# _*_ coding:utf-8 _*_
# __Author:edeyuan
# Version: 1.0
# Time:2018/03/17

###########################################################
# bs4Demo(beautifulsoup 4)
# 爬虫:从网页上, 采集数据
# 模块:urllib, urllib2, requests, bsp, scrapy, lxml...
#
# 1.如何获取标签里面的内容
#   查看网络源代码, 数据放在盒子标签里面的 <div> <title> <a>...
#   解析方式:自带的html.parser   lxml解析速度快,能力更强
#   找到标签里面的内容
##############################################################

# from bs4 import BeautifulSoup  # 从网页下载数据

# html = '<div>you</div><title>girlfirend</title>'
# soup = BeautifulSoup(html, 'html.parser')   # 创建一个对象,解析网页
#
# print soup.div  # 获取标签里面的内容
# print soup.title
#
# print 'this is the first demo for bs4, checkout it out!'

##############################################################
# 2.打开html文件,获取网页内容 a.html
#   open ->打开文件函数
#   prettify ->打印本地文件内容
##############################################################

# html = ""  # 创建一个字符串
# soup = BeautifulSoup(open('a.html'), 'html.parser')
# print soup.prettify()  # 打印本地文件的内容


##############################################################
# 3.html源代码中的标签有很多,怎么获取到想要的内容
#  网页命名, class id等字段来相互区分
#  find方法 find(标签, 属性)
#  class_ 是因为class是python的关键字,所以需要下划线用于区分
##############################################################
# html = '<div class="a">Donny</div>' \
#        '<div class="b">Jerry</div>' \
#        '<div class="c">hattie</div>' \
#        '<div class="d">Jason</div>'
#
# soup = BeautifulSoup(html, 'html.parser')
# aim = soup.find('div', class_="c").text  # since Class is key word in python, we need add "_" for convert to lable; text is fetch text
#
# print aim

##############################################################
# 4.find_all 方法 拿到标签中属性中的内容
##############################################################

# html = '<a href="http://www.baidu.com">百度</a>' \   # <a></a>是放超链接的标签
#        '<div class="a">Donny</div>' \
#        '<div class="b">Jerry</div>' \
#        '<div class="c">hattie</div>' \
#        '<div class="d">Jason</div>'
#
# soup = BeautifulSoup(html, 'html.parser')
# aim = soup.find_all('a')
#
# for item in aim:
#     link = item.get('href')
#     print link


##############################################################
# 5.实例,爬豆瓣,下载图片,统计时间
##############################################################


from bs4 import BeautifulSoup  # 从网页下载数据
import urllib2, urllib
import time
import matplotlib.pyplot as plt

picCounter = 0
url = 'https://www.dbmeinv.com/?&pager_offset={}'  # 测试网址


def crawl(url, pageNum): # 模拟浏览器,加上Headers
    headers = {'User-Agent':'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/64.0.3282.167 Chrome/64.0.3282.167 Safari/537.36'}
    urlX = url.format(pageNum)
    print urlX
    req = urllib2.Request(urlX, headers = headers)  # 用地址创建request实例
    page = urllib2.urlopen(req, timeout = 200)  # 打开网页
    contents = page.read()  # 获取源码
    # print contents
    soup = BeautifulSoup(contents, 'html.parser')
    picLinks = soup.find_all('img')

    for girl in picLinks:
        itemLink = girl.get('src')
        # print itemLink
        global picCounter
        # print picCounter
        urllib.urlretrieve(itemLink, filename = 'images/%s.jpg' %picCounter) #下载图片
        picCounter += 1

if __name__ == '__main__':
    maxNrofPage = 5
    ipage = 1
    usedTime = []
    while ipage <= maxNrofPage:
        startTime = time.clock()
        crawl(url, ipage)
        endTime = time.clock()
        usedTime.append(endTime-startTime)
        print 'page %s'%ipage + ' using time:%s'%usedTime[ipage-1]
        ipage += 1

    # figure()指定图表名称
    plt.figure('run time')
    # '.'标明画散点图，每个散点的形状是个圆
    plt.plot(range(maxNrofPage), usedTime)
    # 将当前figure的图保存到文件result.png
    plt.savefig('runingTime.png')
    # 一定要加上这句才能让画好的图显示在屏幕上
    plt.show()



















