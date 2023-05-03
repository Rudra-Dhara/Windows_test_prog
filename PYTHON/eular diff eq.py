# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 10:55:26 2021

@author: ACER
"""

#Fwd eular
import numpy as np
import matplotlib.pyplot as plt
from math import *
def f(x,y):
    return -5*y
a=0 #starting value of x
b=3; n=10
x=np.linspace(a,b,n)
y1=np.zeros(n)
y1[0]=1# the initial consition
h=(x[1]-x[0])
for i in range(n-1):
    y1[i+1]=y1[i]+h*f(x[i],y1[i])
plt.figure(figsize=(20,20))
plt.grid()
plt.plot(x,y1,color='blue')
print(y1)
# backward eular
# defening function for NR
def df(x,y):
    h1=0.000001
    return (f(x,y+h1)-f(x,y))/h1
    
y2=np.zeros(n)
y2[0]=y1[0]
for i in range(n-1):
    y2[i+1]=y2[i]+h*f(x[i],y2[i])
    while  abs(y2[i+1]-h*f(x[i+1],y2[i+1])-y2[i])>0.001:
        y2[i+1]=y2[i+1]+(y2[i+1]-h*f(x[i+1],y2[i+1])-y2[i])/(df(x[i+1],y2[i+1])+1)
        
        print('loop',y2[i+1])
            
    print('ok')
    y2[i+1]=y2[i]+h*f(x[i+1],y2[i+1])
    
plt.plot(x,y2,color='red')
plt.grid()
plt.show()

print(y2)    
