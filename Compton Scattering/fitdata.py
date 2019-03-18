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

file = ['Cs137_cali2.dat']

f = s.data.fitter()
f.set_functions('A*G(x-x0, sigma)', 'x0, sigma, A', G=Gaussian)
d = np.asarray(s.data.load(file[0]))


y_error = d[1]**(1/2)
f.set_data(x_data = d[0], y_data = d[1], eydata = 2**(1/2))
f.set(sigma = 0.1, ymin = 0)

### CLICK
x_click, y_click = f.ginput()[0]
f.set(xmin = x_click, xmax = x_click )
f.set(A = y_click, x = x_click, plot_guess = False, xlabel = 'TBD',
      ylabel = 'TBD')
f.fit()
print(f)


