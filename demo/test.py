#!/usr/bin/python3
#coding=utf-8

'''
测试着玩，request；
'''

import requests
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4882.400 QQBrowser/9.7.13059.400',
        'referer':'http://www.taobao.com'
    }

chrome_options.add_argument('Accept="text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3"')
browser = webdriver.Chrome(r'D:\soft\chromedriver_win32\chromedriver.exe')
wait = WebDriverWait(browser,10)
data = "H4sIAAAAAAAAAC2Qy3LCMAxF/0XrhLH8kpxdgNAWCn1AH3STSR34Abrr9N97Yxh7ro6la1v2L7XU0Hy97+ebTW8NJ6OcbmAdVdQqDBKz5iRRWL13rIPnMYWT6pmt99HAN4dtu1I22nc9QMItxmtkI303+SyMi91xQkcNGwPw1CAsULlc8pB/LqguJ1+7BHXUBGtnHCpaFeNd0Xtq0GeY0g9ArzFoRWtg4Ki2og01CcVHZKKvaHtd7m7Lp3LIc9EX3LXvy8B9r+UpgH0pHtAllJE9ZzmNacy1qJxrL+67HrJobazlPIpxo1XsO+CN+MA0c8F7kYiMK0e9FX0v+lH0E91UdCz8hV0hsmHBtMb9/QNRAxRWngEAAA=="
#url = "http://www.baidu.com"
url = "http://www.txtwizard.net/compression"

r = browser.get(url)
try:
    element = WebDriverWait(browser, 10).until(lambda x: x.find_element_by_xpath("//div[@class='controls']/textarea"))
finally:
    print("进入解压了吧")
    try:
        browser.find_element_by_xpath("//div[@class='controls']/textarea").send_keys(data)
    except Exception as e:
        print(e)
    else:
        browser.find_element_by_xpath("//button[text()='Decompress']").click()


    time.sleep(5)
    #browser.close()

