#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:25:59 2019

@author: vuongthaian
"""

import spinmob as s
import numpy as np
from numpy import pi, exp, real
from scipy.special import wofz, erf
ROOT2 = 2.0**0.5 # Code speedup


### FITTING
# Voigt function
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
## Initiate file names and stuffs 
files = ['Pb-100-24-01.UXD', 'Pb-75-Sn-25-14-01.UXD', 'Pb-50-Sn-50-14-01.UXD',
         'Pb-25-Sn-75-14-01.UXD', 'Sn-100-10-01.UXD'] 
theta2 = []
theta2_err = []
angle1 = []
error1 = []
angle2 = []
error2 = []

numpeak = 10;
         
for num in range (1,2): 
    # Create a fitter object
    f = s.data.fitter()
    
    
    # Define the fit functions (in this case, the sum of two Lorentzians) 
    # and floating parameters.
    f.set_functions('A1*V(x-x1,s1,a1) + A2*V(x-(x1+0.265),s2,a2) +c',
                    'A1, x1, s1, a1, A2, s2, a2,c=10', V= voigt)
    


    # Load a *.txt data file
    d = s.data.load(files[0])
    
    # Stick the data into the fitter object
    y_error = d[1]**(1/2)
    f.set_data(xdata=d[0][2700:2760], ydata=d[1][2700:2760], eydata=y_error[2700:2760])
              
    
    # Set some of the guess parameters

    f.set(s1 = 0.01, a1 = 0.01, ymin = 10)
    f.set(s2 = 0.01, a2 = 0.01, ymin = 10)
   
    
    # Fun trick: have the user click to make guess parameters!
    print("CLICK THE PEAKS!!")
    click_x1, click_y1 = f.ginput()[0]
    click_x2, click_y2 = f.ginput()[0]
    
    f.set(xmin = click_x1 - 2.5, xmax = click_x1 + 2.5)
    
    
    
    # make a better guess for a and x0, trim the data, and label the axes!
    f.set(A1=click_y1, x1=click_x1, 
          A2=click_y2, 
          plot_guess = True, xlabel = '2'r'$\theta$',
          ylabel = 'Intensity [Counts]')
    
    
    
    # Fit!
    f.trim()
    f.fit()
    
    a = f.results
    angle1.append(a[0][1])
    error1.append(np.sqrt(a[1][1][1]))
    angle2.append(a[0][5])
    error2.append(np.sqrt(a[1][5][1]))
    
        
    
    # show the results (see spinmob wiki for more details!)
    print(f)
#    print(f2)
#    print(f3)
#    print(f4)
    #print(f5)
    
    ## Do data
#    angle = []
#    error = []
#    mylist = [f1, f2, f3, f4]
#    for i in range(1,5):
#        a = mylist[i-1].results
#        angle.append(a[0][1])
#        error.append(np.sqrt(a[1][1][1]))
#    
#    theta2.append(angle)
#    theta2_err.append(error)
    
    







