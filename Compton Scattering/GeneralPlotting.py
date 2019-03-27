# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:55:52 2019

@author: aorfi
"""

import spinmob as s
import numpy as np
import matplotlib.pyplot as plt
from tempfile import TemporaryFile

#peak1 = s.data.load('cuAu-sampleA-14-01.UXD')

rod = s.data.load('al_30deg.dat')
norod= s.data.load('norod_30deg.dat')
x = rod[0]
y = np.zeros(rod[0].size)
for i in range(rod[0].size):
    y[i] = rod[1][i] - norod[1][i]
    
data = np.zeros((2,x.size)) 

for j in range(rod[0].size):
    data[0][j] = x[i]
    
for j in range(rod[1].size):
    data[1][j] = y[j]

#d = s.data.databox()
np.savetxt('30.txt', data, delimiter=' ,')
print(data[1])
print(y)
#data.save_file()
alloy_legend = ["Sample A", "Sample B"]


s.plot.xy.data([rod[0],norod[0],x],\
                [rod[1],norod[1],y],\
                xlabel = 'Bin',\
                ylabel = 'Counts',\
                label = alloy_legend,\
                legend = 'right')
#s.plot.xy.data(peak1[0], peak1[1])
#s.plot.xy.data(peak2[0], peak2[1]