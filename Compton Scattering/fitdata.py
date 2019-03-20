#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 16:25:26 2019

@author: vuongthaian
"""
import spinmob as s
import numpy as np
from numpy import pi, exp, real
from scipy.special import wofz, erf


def Gaussian(x, sigma):
    var = ((x)**2)/(sigma**2)
    return exp(-var)

file = ['Ba133_cali2.dat']

f = s.data.fitter()
f.set_functions('A*G(x-x0, sigma)', 'x0, sigma, A', G=Gaussian)
d = np.asarray(s.data.load(file[0]))


y_error = d[1]**(1/2)
f.set_data(xdata = d[0], ydata = d[1], eydata = y_error)
f.set(sigma = 6)

### CLICK
x_click, y_click = f.ginput()[0]
f.set(xmin = x_click-17, xmax = x_click+12)
f.set(A = y_click, x0 = x_click, plot_guess = False, xlabel = 'TBD',
      ylabel = 'TBD')
f.fit()
print(f)


