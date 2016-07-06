#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import tushare as ts
import matplotlib.pyplot as plt

df = ts.get_h_data('600000', start='1995-01-01', end='2016-06-16')

#绘图
x = df.index
y = df.close
plt.title('600000')
plt.xlabel('date')
plt.ylabel('price')
plt.plot(x,y,"g-")
plt.show()