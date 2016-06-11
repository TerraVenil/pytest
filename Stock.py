# coding: UTF-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import numpy as np
import tushare as ts
import matplotlib.pyplot as plt

df = ts.get_h_data('600000', start='2014-01-01', end='2016-06-16')

x = df.index
y = df.close

plt.title('fuck')
plt.xlabel('时间')
plt.ylabel('价格')
plt.plot(x,y,"g-")

plt.show()