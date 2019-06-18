#! /usr/lib/python3
#coding=utf-8


import requests

'''
爬取笔趣小说网的网页
'''

url = "http://www.biqukan.com/"
url1 = "https://www.biqukan.com/1_1094/5978227.html"

req = requests.get(url1)
print(req.text)
