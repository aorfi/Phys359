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
y = [362.37, 279.59, 40.367, 193.67]
y_error = [0.25, 0.12, 0.041, 0.75]

f = s.data.fitter()
f.set_functions('L(x-x0, m, b)', 'x0, m, b', L = Line)
f.set_data(xdata = x, ydata = y, eydata = y_error)


f.set(b = 0, m = 1)
f.set(plot_guess = False, xlabel = 'Channel', ylabel = 'Count')
f.fit()

print(f)