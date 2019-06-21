#!/usr/bin/python3
#coding=utf-8

'''
测试着玩，request；
'''

import requests
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')

browser = webdriver.Chrome(r'D:\soft\chromedriver_win32\chromedriver.exe',options=chrome_options)
wait = WebDriverWait(browser,10)
data = "H4sIAAAAAAAAAC2Qy3LCMAxF/0XrhLH8kpxdgNAWCn1AH3STSR34Abrr9N97Yxh7ro6la1v2L7XU0Hy97+ebTW8NJ6OcbmAdVdQqDBKz5iRRWL13rIPnMYWT6pmt99HAN4dtu1I22nc9QMItxmtkI303+SyMi91xQkcNGwPw1CAsULlc8pB/LqguJ1+7BHXUBGtnHCpaFeNd0Xtq0GeY0g9ArzFoRWtg4Ki2og01CcVHZKKvaHtd7m7Lp3LIc9EX3LXvy8B9r+UpgH0pHtAllJE9ZzmNacy1qJxrL+67HrJobazlPIpxo1XsO+CN+MA0c8F7kYiMK0e9FX0v+lH0E91UdCz8hV0hsmHBtMb9/QNRAxRWngEAAA=="
url = "http://www.baidu.com"
url1 = "www.txtwizard.net/compression"

r = browser.get(url)

print("进入百度了吧")

time.sleep(5)
browser.close()

