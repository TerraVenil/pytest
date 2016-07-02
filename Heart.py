#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

def func1(x):
    return (16*np.fabs(x) + np.sqrt(22500 - (x**2) * 900)) / 34
def func2(x):
    return (16*np.fabs(x) - np.sqrt(22500 - (x**2) * 900)) / 34

x = np.linspace(-5.0,5.0,50000)
plt.plot(x,func1(x),c='r')
plt.plot(x,func2(x),c='r')
plt.show()