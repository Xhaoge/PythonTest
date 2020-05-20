#!/usr/bin/python3
#coding=utf-8
'''
    此脚本用于一些http请求方面的练习
'''

import requests

class HttpReq():
    pass

url='http://api.gloryholiday.com/mairihm/baggage/test/search'
data = '''
        {"cid": "mairi","productType": 1,
        "routing": {"currency": "USD","fromSegments": [{
        "arrAirport": "LAX",
        "arrTime": "201910131320",
        "cabinGrade": "Y",
        "carrier": "UA",
        "depAirport": "BJS",
        "depTime": "201908152035"}]}}
        '''

response = requests.post(url,data=data)
print(response.text)    #打印原始响应字符串；
print(response.status_code) #200
print(response.json()['fromTrips']) #打印键值对的值；
#print(response.raise_for_status())
