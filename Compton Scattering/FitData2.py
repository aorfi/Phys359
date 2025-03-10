#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 15:24:58 2019

@author: Elisa
"""

import spinmob as s
import numpy as np
from numpy import pi, exp, real
from scipy.special import wofz, erf
import matplotlib.pyplot as plt
from scipy.special import wofz, erf
ROOT2 = 2.0**0.5 # Code speedup


def Gaussian(x, sigma):
    var = ((x)**2)/(sigma**2)
    return exp(-var)

def Line(x, m , b): 
    return m*x + b 

def Step(x, sigma): 
    den = 1.0 + exp(-(1.0/sigma)*x)
    return 1.0 - (1.0)/(den)
    
#OFFSET 
#these are 3 functions that affect the gaussian curve that we are fitting for! 
#with our data, we want to fit the sum of all 3 + offset 
#check with the website written down: https://www.nndc.bnl.gov/nudat2/chartNuc.jsp 
#for whether or not we have more than 1 peak that we should be fitting (generally, start fitting 1 peak and see)

#gaussian and step should have the same x_0 and the same sigma 


d = np.transpose(np.asarray(np.loadtxt('Cs137_cali2.dat')))
d_x = d[0][320:400]
d_y = d[1][320:400]


f = s.data.fitter()

f.set_functions('A1*G(x-x0, s) + A2*S(x-x0, s) + L(x,m,b)', 'A1, x0, s, A2, m,b', G= Gaussian, S = Step, L=Line) 


y_error = d_y**(1/2)

f.set_data(xdata = d_x, ydata = d_y, eydata = y_error)
f.set(s = 15, b=1)

click_x1, click_y1 = f.ginput()[0]
click_x2, click_y2 = f.ginput()[0]
click_x3, click_y3 = f.ginput()[0]
f.set(x0 = click_x1, A1= click_y1, A2 = click_y2 - click_y1, m = 
      (click_y3 - click_y2)/(click_x3-click_x2), plot_guess = False, xlabel = 'Channel',
      ylabel = 'Count')
f.set(plot_guess = False, ymin = 2)
f.fit()
print(f)


s.plot.xy.function('exp(-((x-360)**2)/(18**2))', 300,400)
#s.tweaks.integrate_shown_data()
#s.plot.xy.function('1.0 - (1.0)/(1.0 + exp(-(1.0/18.26)*x))', -20, 20)

### FOR Cs137
#d_x = d[0][320:400]
#d_y = d[1][320:400]

### FOR Na22
#d_x = d[0][250:310]
#d_y = d[1][250:310]

### FOR Ba133 Rigth most
#d_x = d[0][179:209]
#d_y = d[1][179:209]

### FOR Ba133 Left most
#d_x = d[0][32:47]
#d_y = d[1][32:47]

### FOR Ba133 Right most (more data)
#d_x = d[0][179:213]
#d_y = d[1][179:213]

### FOR Zero 15deg
#d_x = d[0][335:395]
#d_y = d[1][335:395]
