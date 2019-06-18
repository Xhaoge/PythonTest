#! /usr/lib/python3
#coding=utf-8


import requests

'''
爬取笔趣小说网的网页
'''

url = "http://www.biqukan.com/"
url1 = "https://www.biqukan.com/1_1094/5403177.html"

# req = requests.get(url1)
# print(req.text)


'''
爬取高清图片
'''

url3 = "https://unsplash.com/"
req = requests.get(url=url3)
print(req.text)
