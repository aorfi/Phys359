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
name_rod = ['ENal_25deg.dat','ENal_30deg.dat','ENal_35deg.dat','ENal_40deg.dat','ENal_42deg.dat','ENal_45deg.dat']
name_norod = ['ENnorod_25deg.dat','ENnorod_30deg.dat','ENnorod_35deg.dat','ENnorod_40deg.dat','ENnorod_42deg.dat','ENnorod_45deg.dat']


### INTITIATE DATA
angle = np.asarray([25,30,35,40,42,45])*np.pi/180
#angle_er = 

time = [400.78000000000003, 400.7 ,400.48, 401.5, 400.78000000000003, 400.56]
total_count = np.zeros(angle.size)
#total_count_er = 

for i in range(angle.size):
    rod = s.data.load(name_rod[i])
    norod = s.data.load(name_norod[i])
    sub = rod[1] - norod[1]
    half_max = max(sub)/2
    total = 0
    
    for j in range(sub.size):
        if sub[j]<half_max:
            total = total + sub[j]
    total_count[i] = total

rate = total_count/time
#rate_er = 

def KNformula(x):
    right = (1+np.cos(x)**2)/(1+alpha*(1-np.cos(x)))**2
    top = alpha**2 * (1-np.cos(x))**2
    bot = (1+np.cos(x)**2)*(1+alpha*(1-np.cos(x)))
    left = 1 + top/bot
    return (1/2)*left*right

x_data = KNformula(angle)

plt.plot(x_data, rate, '.')
plt.show()

    


