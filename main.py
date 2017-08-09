# -*- coding: utf-8 -*-
# filename: main.py

import sys
import csv

from urllib import urlopen
from bs4 import BeautifulSoup
from house_info import house

#将从citys.csv 文件中读取的城市信息保存到字典中
def get_city_dict():
    #创建城市字典,保存信息
    city_dict = {}

    #将citys.csv中的数据读取到city_dict中
    with open("citys.csv","r") as f:
        reader = csv.reader(f)
        for city in reader:
            # {city_name:city_url}
            city_dict[city[0]] = city[1]
    return city_dict

#将城市对应的区域信息保存到字典中
def get_district_dict(url):
    #将信息保存到字典中
    district_dict = {}
    html = urlopen(url).read()
    bsobj = BeautifulSoup(html,"html5lib")
    roles = bsobj.find("div",{"data-role":"ershoufang"}).findChildren("a")
    for role in roles:
        #对应区域的url
        district_url = role.get("href").encode("utf-8")
        #对应区域名称
        district_name = role.get_text().encode("utf-8")
        #保存在字典中
        district_dict[district_name] = district_url
    return district_dict
def run():
    city_dict = get_city_dict()
    #打印城市名
    for city in city_dict.keys():
        print city,
    print
    #与用户交互,获取用户输入
    input_city = raw_input("请输入城市: ")
    #根据用户输入的城市名,得到城市的url
    city_url = city_dict.get(input_city)
    if not city_url:
        print "输入错误"
        #退出
        sys.exit()

    #ershoufang_city_url = city_url + "ershoufang"
    ershoufang_city_url = city_url
    district_dict = get_district_dict(ershoufang_city_url)
    #打印区域名
    for district in district_dict.keys():
        print district,
    print

    input_district = raw_input("请输入区域名: ")
    district_url = district_dict.get(input_district)

    #输入错误,退出程序
    if not district_url:
        print "输入错误"
        sys.exit()
        #如果输入正确
    else:
        house_info_url = city_url + district_url[12:]
        print house_info_url
        house(house_info_url)

if __name__ == "__main__":
    run()
