# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 17:48:09 2019

@author: aorfi
"""

import spinmob as s
import numpy as np
import matplotlib.pyplot as plt
import math



#peak values
#these are super rough 
x1 = 661.62 
y1 = 697.9469170217355

x2 = 655.22
y2 = 369.5710232820564

x3 = 653.6 
y3 = 109.96237826344539

x4 = 653.2
y4 = 39.097251441522126

x_values = [0.094,0.162,0.254,0.322]
y_values = np.asarray([y1,y2,y3,y4])

ytest = np.zeros(4)
for i in range (0,3):
    ytest[i] = 120000*math.exp(-1*x_values[i])
    

#s.plot.xy.data([x_values,x_values],[y_values,ytest])

f = s.data.fitter()
a = 19.7666 
f.set_functions('I*e**(-a*x)','I,a') 

y_error = y_values**(1/2)

f.set_data(xdata = x_values, ydata = y_values , eydata = y_error)
f.set(I = 5000)


f.set(plot_guess = True, xlabel = 'thickness',
      ylabel = 'I')

f.fit()
print(f)
    