# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:48:09 2019

@author: aorfi
"""

import spinmob as s
import numpy as np
import matplotlib.pyplot as plt
import math

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

x_values = [0.094,0.162,0.254,0.322]
y_values = [y1,y2,y3,y4]

ytest = np.zeros(4)
for i in range (0,3):
    ytest[i] = 120000*math.exp(-1*x_values[i])
    

#s.plot.xy.data([x_values,x_values],[y_values,ytest])

f = s.data.fitter()
a = 3466 #check this
f.set_functions('I*e**(-0.08236*x)','I') 

y_error = 100

f.set_data(xdata = x_values, ydata = y_values , eydata = y_error)
f.set(I = 120000)


f.set(plot_guess = True, xlabel = 'thickness',
      ylabel = 'I')

f.fit()
print(f)
    