# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:55:52 2019

@author: aorfi
"""

import spinmob as s
import numpy as np
import matplotlib.pyplot as plt
from tempfile import TemporaryFile

#TO SAVE SUBTRACTED DATA!

#peak1 = s.data.load('cuAu-sampleA-14-01.UXD')

rod = s.data.load('al_20deg.dat')
norod = s.data.load('norod_20deg.dat')
brick = s.data.load('3brick.dat')


x = rod[0]

rod_eff = np.zeros(rod[0].size)
norod_eff = np.zeros(rod[0].size)
brick_eff = np.zeros(brick[0].size)
for i in range(rod[0].size):
     a = x[i]
     eff = 1/100*(2.5*10**(-12)*a**5 - 6.3*10**(-9)*a**4 + 5.9*10**(-6)*a**3 - 0.0023*a**2 + 0.17*a + 95) #efficiancy curve
     rod_eff[i] = rod[1][i]/eff
     norod_eff[i] = norod[1][i]/eff
     brick_eff[i] = brick[1][i]/eff




y = np.zeros(rod[0].size)#for rod-nonrod
for i in range(rod[0].size):
    y[i] = rod[1][i] - norod[1][i]
ye = np.zeros(rod[0].size)#for efficieny division
for i in range(rod[0].size):
    ye[i] = rod_eff[i] - norod_eff[i]


data = np.zeros((2,x.size))

for j in range(rod[0].size):
    data[0][j] = x[j]

for j in range(rod[1].size):
    data[1][j] = ye[j]
    
brick_data = np.zeros((2,x.size))

for j in range(brick[0].size):
    brick_data[0][j] = brick[0][j]

for j in range(brick[1].size):
    brick_data[1][j] = brick_eff[j]





# =============================================================================
# alloy_legend = ["Rod", "No Rod", "Subtraction", "Efficiancy"]
# 
# 
# 
# s.plot.xy.data([rod[0],norod[0],x,x],\
#                  [rod[1],norod[1],y,ye],\
#                  xlabel = 'Bin',\
#                  ylabel = 'Counts',\
#                  label = alloy_legend,\
#                  legend = 'right')
# =============================================================================


s.plot.xy.data(brick_data[0], brick_data[1])


#now, x and y are the data from subtracting rod and no rod.
np.savetxt('3brickX.txt', np.transpose(brick_data[0]), delimiter =' ')
np.savetxt('3brickY.txt', np.transpose(brick_data[1]), delimiter =' ')
#np.savetxt('20edegX.txt', np.transpose(data[0]), delimiter =' ')
#np.savetxt('20edegY.txt', np.transpose(data[1]), delimiter =' ')
