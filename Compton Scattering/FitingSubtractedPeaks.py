#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 12:54:47 2019

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



#dx = np.asarray(np.loadtxt('20edegX.txt', delimiter=' '))
#dy = np.asarray(np.loadtxt('20edegY.txt', delimiter=' '))
#y_sum = np.asarray(np.loadtxt('20edegY_error.txt'))
    
data = s.data.load('2brickEFF.dat')
dx = data[0]
dy = data[1]

f = s.data.fitter()

#f.set_functions('A1*G(x-x0, s) + A2*S(x-x0, s) + L(x,m,b)', 'A1, x0, s, A2,m,b', G= Gaussian, S = Step, L = Line) 
f.set_functions('A1*G(x-x0, s) + A2*S(x-x0, s)', 'A1,x0,s,A2', G = Gaussian, S = Step)

y_error = dy**(1/2)

f.set_data(xdata = dx, ydata = dy, eydata = y_error)
f.set(s = 50)#, b=0)

click_x1, click_y1 = f.ginput()[0]
click_x2, click_y2 = f.ginput()[0]
click_x3, click_y3 = f.ginput()[0]
f.set(xmin = click_x1 - 100, xmax = click_x1 + 100)

f.set(x0 = click_x1, A1= click_y1, A2 = click_y2 - click_y3,  plot_guess = True, xlabel = 'Channel',
      ylabel = 'Count')
f.set(plot_guess = True, ymin = 1)
f.fit()
print(f)

A1, x0, s1, A2, m, b = f.results[0]
x = dx
step = A2*Step(x-x0, s1)
Gua = A1*Gaussian(x-x0, s1)
#l = Line(x, m,b )


alloy_legend = ["Rod", "Gaussian", "Step Function"]
s.plot.xy.data([dx,dx,dx,dx],\
                  [dy,l, Gua,step],\
                  xlabel = 'Bin',\
                  ylabel = 'Counts',\
                  label = alloy_legend,\
                  legend = 'right')

#f(plot_all_data = True)