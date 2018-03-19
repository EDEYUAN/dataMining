# _*_ coding: utf-8 _*_

#time:2018/03/17 12:21:00
#version: 1.0
#__author__: edeyuan

import urllib2
import re
from cons import headers
from simplejson import loads


def getUrlList():
    req = urllib2.Request('https://mm.taobao.com/tstar/search/tstar_model.do?_input_charset=utf-8')
    req.add_header('user-agent',headers())
    #因为是POST,不是GET,所以需要data    
    html = urllib2.urlopen(req,data='q&viewFlag=A&sortType=default&searchStyle=&searchRegion=city%3A&searchFansNum=&currentPage=1&pageSize=100')

    print 'sds'
    print html
    html.read().decode('gbk').encode('utf-8')
    print html

    # #返回数据是json(类似于字符串,可以用正则取出来,但是复杂点),我们需要里面数据的切片,所以先转化为dict,然后字典取值
    # #所以我们需要import json中的loads
    json = loads(html)
    return json['data']['searchDOList']

def getInfo(userId):
    req = urllib2.request('https://mm.taobao.com/self/aiShow.htm?&userId=%s' %userId)
    req.add_header('user-agent',headers())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    #print html
    return html
    

def getAlbumList(userId):
    req = urllib2.request('https://mm.taobao.com/self/model_album.htm?&user_id=' %userId)
    req.add_header('user-agent',headers())
    html = urllib2.urlopen(req).read().decode('gbk').encode('utf-8')
    #print html
    
    reg = r'class="mm-first" href="//(.*?)"'
    return re.findall(reg,html)[::2]



# #获取到所有的基本信息了
for i in getUrlList():
    print i['realname']
    # userId = i['userId']
    #getInfo(userId) #获取个人页面






