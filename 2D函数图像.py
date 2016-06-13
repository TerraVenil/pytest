#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

func = lambda x : x**2 + 8

x = np.linspace(-10,10,300)
y = func(x)

plt.plot(x,y,'r-')
plt.title('y = x^2 + 8')
plt.xlabel('x')
plt.ylabel('y')

plt.show()