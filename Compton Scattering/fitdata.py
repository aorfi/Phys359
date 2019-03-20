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

#TA suggestion: try double peak fitting for Na and Ba: 

file = ['']

f = s.data.fitter()
#f.set_functions('A*G(x-x0, sigma)', 'x0, sigma, A', G=Gaussian) #FOR GAUSS
f.set_functions('A1*G(x-x1,s1) + A2*G(x-x2, s2)', 'A1, x1, s1, A2, x2, s2', G= Gaussian) #for double peak 
d = np.asarray(s.data.load(file[0]))


y_error = d[1]**(1/2)
f.set_data(xdata = d[0], ydata = d[1], eydata = y_error)
#f.set(sigma = 6, ymin = 0) #FOR GAUSS
f.set(s1 = 6, s2=6)

### CLICK
click_x1, click_y1 = f.ginput()[0]
click_x2, click_y2 = f.ginput()[0]
f.set(xmin = click_x1-20, xmax = click_x2+20)
f.set(A1 = click_y1, x1 = click_x1, A2 = click_y2, x2 = click_x2, plot_guess = False, xlabel = 'channel',
      ylabel = 'count')
f.fit()
print(f)




