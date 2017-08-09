# -*- coding: utf-8 -*-
# filename:pics

import csv
import numpy
import matplotlib.pyplot as plt

price,size = numpy.loadtxt("house.csv",delimiter='|',usecols=(1,2),unpack=True)

plt.figure()
plt.subplot(211)
plt.title("price")
plt.title("/10000RMB")
plt.hist(price,bins=30)

plt.subplot(212)
plt.title("area")
plt.figure(2)
plt.title("price")
plt.plot(price)

plt.show()
