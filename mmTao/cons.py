# _*_ coding: utf-8 _*_

#time:2018/03/17 12:21:00
#version: 1.0
#__author__: edeyuan

import random


headerStr = '''Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'''

def headers():
    header = headerStr.split('\n')
    length = len(header)
    return header[random.randint(0,length-1)]

