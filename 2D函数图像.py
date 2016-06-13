#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

func = lambda x : x*2 + 1

x = np.linspace(-100,100,300)
y = func(x)

plt.plot(x,y,'r-')
plt.title('y = 2x + 1')
plt.xlabel('x')
plt.ylabel('y')

plt.show()