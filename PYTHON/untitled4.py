# -*- coding: utf-8 -*-
"""
Created on Thu May 12 22:26:26 2022

@author: ACER
"""

import numpy as np
import matplotlib.pyplot as plt
import math
#define the function
def wf(r,theta):
    return np.exp(-(r**2)/2)
arr_r=np.arange(0.0,30,.1)
arr_theta=np.linspace(0,360,1000)
r,theta = np.meshgrid(arr_r,arr_theta)
m=10
z=(r**(2*(m-2)))*wf(r,theta)*(r**4/2-3*m*r**2+4*m*(m-1))**2/math.factorial(m)

fig, ax = plt.subplots(dpi=120,subplot_kw=dict(projection='polar'))
ax1= ax.contourf(theta, r, z, 500, cmap='plasma')
fig.colorbar(ax1)