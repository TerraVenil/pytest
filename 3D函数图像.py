#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d

x, y = np.mgrid[-10:10:50j, -10:10:50j]
z = x**2 + y**2

ax = plt.subplot(111, projection = '3d')
ax.plot_surface(x, y, z, rstride=2, cstride=1, cmap=cm.jet, alpha=0.8)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('z = x^2 + y^2')

plt.show()
