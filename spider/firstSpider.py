#coding=utf-8

import urllib
import re
from bs4 import BeautifulSoup


response = urllib.urlopen("https://www.douyu.com/")  # 这时候 response 是一个对象 需要读取(read)一下
html = response.read()  # type(html)  -> str
# firstLine = html.read()
# print(html.info())
# urllib.urlretrieve("https://ss0.bdstatic.com/5aV1bjqh_Q23odCf/static/superman/img/logo/bd_logo1_31bdc765.png", "baidu.jpg")

soup = BeautifulSoup(html)  # 把他变成 bs 对象
# 这个select可以链式调用
# soup.select()

# 正则匹配出错
# imgList = re.findall('src="(.*?\.(jpg|png))"', html)
'''
j = 0
for i in imgList:
    imgUrl = i[0]
    urllib.urlretrieve(imgUrl, './img/%d.jpg'%j)
    j += 1
'''