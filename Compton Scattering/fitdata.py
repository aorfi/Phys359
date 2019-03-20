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
import matplotlib.pyplot as plt
from scipy.special import wofz, erf
ROOT2 = 2.0**0.5 # Code speedup


def voigt(x, sigma, gamma):
    """
    Returns a Voigt function (a convolution of a Lorentzian and Gaussian) 
    centered at x=0 with Gaussian standard deviation sigma and Lorentzian 
    half-width gamma. The function is normalized to have unity area.
    
    Parameters
    ----------
    x:
        Distance from center of peak.
    sigma = 1:
        Standard deviation of Gaussian ~ exp(-x**2/(2*sigma**2)) 
    gamma = 1:
        Halfwidth of Lorentzian ~ 1/(1+x**2/gamma**2)
    """
    return real(wofz((x + 1j*gamma)/sigma/ROOT2)) / sigma / (2*pi)**0.5    

def Gaussian(x, sigma):
    var = ((x)**2)/(sigma**2)
    return exp(-var)

file = ['Ba133_cali2.dat']

f = s.data.fitter()
#f.set_functions('A*G(x-x0, sigma)', 'x0, sigma, A', G=Gaussian) #FOR GAUSS
f.set_functions('A*V(x-x0,s,a)', 'A, x0, s, a', V= voigt)
d = np.asarray(s.data.load(file[0]))


y_error = d[1]**(1/2)
f.set_data(xdata = d[0], ydata = d[1], eydata = y_error)
#f.set(sigma = 6, ymin = 0) #FOR GAUSS
f.set(s = 6, a = 0.2)

### CLICK
x_click, y_click = f.ginput()[0]
f.set(xmin = x_click-20, xmax = x_click+20)
f.set(A = y_click, x0 = x_click, plot_guess = False, xlabel = 'TBD',
      ylabel = 'TBD')
f.fit()
print(f)




