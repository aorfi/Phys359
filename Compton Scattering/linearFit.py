#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:51:05 2019

@author: vuongthaian
"""

import spinmob as s
import numpy as np
from numpy import pi, exp, real
from scipy.special import wofz, erf
import matplotlib.pyplot as plt
from scipy.special import wofz, erf
ROOT2 = 2.0**0.5 # Code speedup 


def Line(x, m , b): 
    return m*x + b 

x = [661.6, 511, 81, 356]
y = [362.88, 279.59 , 40.367, 193.67]
y_error = [0.41, 0.12 ,0.044, 0.75]

#y = [366.39, 283.197, 41.141, 194.82]
#y_error = [0.17, 0.075, 0.044, 0.26]

f = s.data.fitter()
f.set_functions('L(x, m, b)', 'm, b', L = Line)
f.set_data(xdata = x, ydata = y, eydata = y_error)


f.set(b = 0, m = 1)
f.set(plot_guess = False, xlabel = 'Energy', ylabel = 'Channel')
f.fit()

print(f)