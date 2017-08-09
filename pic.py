# -*- coding: utf-8 -*-
import csv
import numpy
import matplotlib.pyplot as plt

#读取house.csv文件中价格和面积列
price,size = numpy.loadtxt('house.csv',delimiter='|',usecols=(1,2),unpack=True)
print price
print size

#求价格和面积的平均
price_mean = numpy.mean(price)
size_mean = numpy.mean(size)

print "平均价格: ",price_mean
print "平均面积为: ",size_mean

#求价格和面积的方差
price_var = numpy.var(price)
size_var = numpy.var(size)

print "价格的方差为: ",price_var
print "面积的方差为: ",size_var
