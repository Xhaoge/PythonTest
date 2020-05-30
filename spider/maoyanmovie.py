#!/usr/lib/python3
#coding=utf-8

'''
进行猫眼电影排行Top100抓取
'''
import json
import re
from multiprocessing.pool import Pool
import requests
from requests.exceptions import RequestException

#获取一页的内容；
def get_one_page(url):
    try:
        response = requests.get(url)
        print("url: ",url)
        if response.status_code == 200:
            response.encoding = "utf-8"
            print(response.text)
            print(type(response.text))
            print(response.encoding)
            return response.text
        return None
    except RequestException as e:
        return e

#利用正则抓取想要的信息；
def parse_one_page(html):
    print("=======================")
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                          +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>''',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield{
            "index":item[0],
            "image":item[1],
            "title":item[2],
            "actor":item[3].strip()[3:],
            "time":item[4].strip()[5:],
            "score":item[5]+item[6]
        }

#将获取的内容逐条写进文件中；
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii = False)+'\n')
        f.close()

def main():
    # url = "http://maoyan.com/board/4?offset="+str(offset)
    url = "https://www.baidu.com"
    html = get_one_page(url)
    # print("html: ",html)
    # print(html)
    # for item in parse_one_page(html):
    #     write_to_file(item)


if __name__ == "__main__":
    main()
    # for i in range(0,100,10):
    #     main(i)
    # # 多进程替代单进程的爬取内容，不足之处便是顺序的问题；
    # pool = Pool()
    # pool.map(main,[i for i in range(0,100,10)])
