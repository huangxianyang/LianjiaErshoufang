# -*- coding: utf8 -*-
# filename: citys.py

import csv
from urllib import urlopen
from bs4 import BeautifulSoup

url = "https://www.lianjia.com"

#获取 html 页面
html = urlopen(url).read()

#获取Beautifulsoup 对象,用HTML5lib解析,也可以用xml解析,html5lib容错性较好,所以此处用html5lib
bsobj = BeautifulSoup(html,"html5lib")

#得到class = "fc-main clear"的div下所有a标签
city_tags = bsobj.find("div",{"class":"link-list"}).div.dd.findChildren("a")

#将每一条数据抽离,保存到citys.csv文件中
with open("citys.csv","w") as f:
    writ = csv.writer(f)
    for city_tag in city_tags:
        #获取<a>标签的href链接
        city_url = city_tag.get("href").encode("utf-8")
        #获取<a>标签的文字
        city_name = city_tag.get_text().encode("utf-8")
        writ.writerow((city_name,city_url))
        print city_name,city_url
