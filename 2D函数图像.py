#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10,10,300)
y = x**2 + 8

plt.plot(x,y,'r-')
plt.title('y = x^2 + 8')
plt.xlabel('x')
plt.ylabel('y')

plt.show()