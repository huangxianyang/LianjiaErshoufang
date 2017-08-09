# -*- coding: utf-8 -*-
# filename: house_info.py
# /usr/bin/python2.7
#库文件
import sys
import re
import csv
import urllib
from bs4 import BeautifulSoup

#成功打印页面时返回页面对象,否则打印错误信息,退出程序
def get_bsobj(url):
    page = urllib.urlopen(url)
    #状态码为 200 时页面成功打开
    if page.getcode() == 200:
        html = page.read()
        bsobj = BeautifulSoup(html,"html5lib")
        return bsobj
    else:
        print "页面错误"
        sys.exit()

#将页面中每一条房屋信息保存为一个字典,将所有的子弹保存在列表中,返回列表
def get_house_info_list(url):
    house_info_list = []
    bsobj = get_bsobj(url)
    if not bsobj:
        return None

    house_list = bsobj.find_all("li",{"class":"clear"})
    for house in house_list:
        #标题
        title = house.find("div",{"class":"title"}).get_text().encode("utf-8")

        #获取信息数据(例如:城市花园|3室1厅 | 120平米|东|精装).通过|符号分隔字符串
        info = house.find("div",{"class":"houseInfo"}).get_text().split("|")

        #小区(例如:城市花园),strip()取出字符串两边的空格,encode将字符串编码utf8
        block = info[0].strip().encode("utf-8")

        #房型
        house_type = info[1].strip().encode("utf-8")

        #面积大小
        size_info = info[2].strip()
        size = re.findall(r"\d+",size_info)[0]

        #价格
        price_info = house.find("div",{"class":"totalPrice"}).span.get_text()
        price = re.findall(r"\d+",price_info)[0]

        #添加到列表中
        house_info_list.append({
            "title":title,
            "price":int(price),
            "size":int(size),
            "block":block,
            "house_type":house_type
        })
    return house_info_list

#读取三个页面的房屋信息,将信息保存到house.csv文件中
def house(url):
    house_info_list = []

    #range(3),即是前三个页面
    for i in range(4):
        new_url = url + "pg" + str(i+1)
        house_info_list.extend(get_house_info_list(new_url))

    if house_info_list:
        #将数据保存到house.csv文件中
        with open("house.csv","wb+") as f:
            #writer 对象,修改默认分隔符为 "|"
            writer = csv.writer(f,delimiter ="|")
            for house_info in house_info_list:
                title = house_info.get("title")
                price = house_info.get("price")
                size =  house_info.get("size")
                block = house_info.get("block")
                house_type = house_info.get("house_type")
                writer.writerow([title,int(price),int(size),block,house_type])
                print block,price,size
