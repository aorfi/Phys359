#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 13:55:55 2019

@author: vuongthaian
"""

import spinmob as s
import numpy as np
from numpy import pi, exp, real
from scipy.special import wofz, erf
import matplotlib.pyplot as plt

## Initiating the fit

f = s.data.fitter()
f.set_functions('m*x + c', 'm, c')

## DATA
y = np.asarray([361.56, 278.808, 39.204, 193.503])
x = np.asarray([661.6, 511, 81, 356])

y_error = np.asarray([0.19, 0.038, 0.011,0.04])

## FIT Parameters
f.set_data(xdata = x, ydata = y, eydata = y_error)
f.set(m = 1, c = 0)

### CLICK
f.set(plot_guess = False, xlabel = 'TBD',
      ylabel = 'TBD')
f.fit()
print(f)