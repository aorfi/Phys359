#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 16:44:41 2019

@author: vuongthaian
"""

import spinmob as s
import numpy as np
import matplotlib.pyplot as plt
me = 511
E0 = 661.657
alpha = E0/me

### FILE NAME
name_rod = ['ENal_25deg.dat','ENal_30deg.dat','ENal_35deg.dat','ENal_40deg.dat']#,'ENal_42deg.dat','ENal_45deg.dat']
name_norod = ['ENnorod_25deg.dat','ENnorod_30deg.dat','ENnorod_35deg.dat','ENnorod_40deg.dat']#,'ENnorod_42deg.dat','ENnorod_45deg.dat']

#i = 5
#x1 = s.data.load(name_rod[i])[0]
#x2 = s.data.load(name_norod[i])[0]
#y1 = s.data.load(name_rod[i])[1]
#y2 = s.data.load(name_norod[i])[1]
##
#s.plot.xy.data([x1],[y1-y2],
#               xlabel = 'Bin',
#               ylabel = 'Counts')

## INTITIATE DATA
angle = np.asarray([25,30,35,40])*np.pi/180
#angle_er = 

time = [400.78000000000003, 400.7 ,400.48, 401.5]#, 400.78000000000003, 400.56]
total_count = np.zeros(angle.size)


for i in range(angle.size):
    rod = s.data.load(name_rod[i])
    norod = s.data.load(name_norod[i])
    sub = rod[1] - norod[1]
    half_max = max(sub)/2
    total = 0
    if i == 0:
        start = 450
    elif i == 1: 
        start = 450
    elif i == 2:
        start = 400
    else:
        start = 400     
    for j in range(sub.size):
        if (sub[j] >= half_max) and (norod[0][j] > start):
            total = total + sub[j] + norod[1][j]
    total_count[i] = total

rate = total_count/time
#rate_er = 

def KNformula(x):
    left = (1+np.cos(x)**2)/(1+alpha*(1-np.cos(x)))**2
    top = alpha**2 * (1-np.cos(x))**2
    bot = (1+np.cos(x)**2)*(1+alpha*(1-np.cos(x)))
    right = 1 + top/bot
    return (1/2)*left*right

def Thompson(x):
    return (1/2)*(1+np.cos(x)**2)

x_data = KNformula(angle)
#x_data = Thompson(angle)

#plt.plot(x_data, rate, '.')
#plt.show()

### FITTING
f = s.data.fitter()
f.set_functions('m*x+b','m,b')
y_error = np.sqrt(total_count)/time
f.set_data(xdata = x_data, ydata = rate , eydata = y_error)
f.set(m = 1, b = 2)
f.set(plot_guess = True, xlabel = 'thickness',
      ylabel = 'I')
f.fit()
print(f)



#    
#
#
