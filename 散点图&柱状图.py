#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

# 散点图
fig1 = plt.figure('scatter')
x = np.random.normal(0, 1, size = 10000)
y = np.random.normal(0, 1, size = 10000)
plt.figure('scatter')
plt.scatter(x, y)
plt.title('Scatter')
plt.xlabel('x')
plt.ylabel('y')

# 柱状图
fig2 = plt.figure('bar')
plt.figure('bar')
plt.hist(x, bins=100)  # 100个柱子
plt.title('Bar')
plt.xlabel('value')
plt.ylabel('counts')

plt.show()