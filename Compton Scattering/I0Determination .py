# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:48:09 2019

@author: aorfi
"""

import spinmob as s
import numpy as np
import matplotlib.pyplot as plt

dx = np.asarray(np.loadtxt('1brickX.txt', delimiter=' '))
dy = np.asarray(np.loadtxt('1brickY.txt', delimiter=' '))

#peak values
#these are super rough 
x1 = 368.845 #368.845 +/- 0.095
y1 = 128042.69933288457

x2 = 365.6 #365.6 +/- 0.18
y2 = 71460.01945025446

x3 = 363.59 #363.59 +/- 0.47
y3 = 20323.243740714344

x4 = 365.22# 365.22 +/- 0.89
y4 = 7093.71560223599

x_values = [x3,x4,x2,x1]
y_values = [y3,y4,y2,y1]

s.plot.xy.data(x_values,y_values)

    