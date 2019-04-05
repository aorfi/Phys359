#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:20:21 2019

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

def Quad(x,a,b,c):
    return a*x**2 + b*x + c
    
#OFFSET 
#these are 3 functions that affect the gaussian curve that we are fitting for! 
#with our data, we want to fit the sum of all 3 + offset 
#check with the website written down: https://www.nndc.bnl.gov/nudat2/chartNuc.jsp 
#for whether or not we have more than 1 peak that we should be fitting (generally, start fitting 1 peak and see)

#gaussian and step should have the same x_0 and the same sigma 

#
data = s.data.load('1brickEFF.dat')
dx = data[0]
dy = data[1]
y_error = (dy)**(1/2)
#
#
##FIRST: fit for background line: 
#g = s.data.fitter()
#g.set_functions('L(x,m,b)', 'm,b', L= Line)   
#g.set_data(xdata = dx, ydata = dy, eydata = y_error)
#
#g.set(xmin = 750, xmax = 1000)
#g.set(ymin = 1)
#
#click_x1, click_y1 = g.ginput()[0]
#click_x2, click_y2 = g.ginput()[0]
#
#g.set(b=0, m = (click_y2 - click_y1)/(click_x2-click_x1),  plot_guess = True, xlabel = 'Channel',
#      ylabel = 'Count')
#
#
#g.fit()
#print(g)
#
#m1,b1 = g.results[0]
#
#f = s.data.fitter()
#
#def fitfunction(x, A1, x0, s, A2):
#    return A1*Gaussian(x-x0, s) + A2*Step(x-x0, s)+ Line(x,m1,b1)
#    
#f.set_functions('fit(x, A1, x0, s, A2)', 'A1, x0, s, A2', fit=fitfunction) 
#f.set_functions('A1*G(x-x0, s) + A2*S(x-x0, s)', 'A1,x0,s,A2', G = Gaussian, S = Step)
#
#
#
#f.set_data(xdata = dx, ydata = dy, eydata = y_error)
#f.set(s =25)
#
#click_x1, click_y1 = f.ginput()[0]
#click_x2, click_y2 = f.ginput()[0]
#click_x3, click_y3 = f.ginput()[0]
#f.set(xmin = 500, xmax = 800)
#
#f.set(x0 = click_x1, A1= click_y1, A2 = click_y2 - click_y3,  plot_guess = True, xlabel = 'Channel',
#      ylabel = 'Count')
#f.set(plot_guess = True, ymin = 1)
#f.fit()
#print(f)
#
#A1, x0, s1, A2= f.results[0]
#x = dx
#step = A2*Step(x-x0, s1)
#Gua = A1*Gaussian(x-x0, s1)
#l = Line(x, m1, b1)
#
##
#alloy_legend = ["Rod", "Gaussian", "Step Function", "Background"]
#s.plot.xy.data([dx,dx,dx,dx],\
#                  [dy,Gua,step,l],\
#                  xlabel = 'Bin',\
#                  ylabel = 'Counts',\
#                  label = alloy_legend,\
#                  legend = 'right')

#f(plot_all_data = True)

                                #USING QUADRATIC AS BACKGROUND FIT: 
##    
g = s.data.fitter()
g.set_functions('Q(x,a,b,c)', 'a,b,c', Q= Quad)   
g.set_data(xdata = dx, ydata = dy, eydata = y_error)

g.set(xmin = 750, xmax = 1000)
g.set(ymin = 1)

g.set(b=1,a=1,c=1,  plot_guess = True, xlabel = 'Channel',
      ylabel = 'Count')
g.fit()
print(g)
a1,b1,c1 = g.results[0]
#
f = s.data.fitter()

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

def fitfunction2(x, A1, x0,x1, s, g, A2, A, A3, v):
    return A1*Gaussian(x-x0, s)  + A*Quad(x,a1,b1,c1) + A2*Step(x-x1, g) + A3*np.sin(v*x)
     
f.set_functions('ft(x, A1, x0, x1, s, g, A2, A, A3, v)+c' , 'A1, x0, x1, s, g, A2, A, A3, v, c=0', ft=fitfunction2) 


f.set_data(xdata = dx, ydata = dy, eydata = y_error)
f.set(s = 15, g = 15 , A = 1, A3 = 1, v = np.pi)

click_x1, click_y1 = f.ginput()[0]
click_x2, click_y2 = f.ginput()[0]
click_x3, click_y3 = f.ginput()[0]
f.set(xmin = 500, xmax = 800)

f.set(x0 = click_x1, A1= click_y1 ,A2 = click_y2 - click_y3, x1 = click_x1, plot_guess = True, xlabel = 'Channel',
      ylabel = 'Count') 
f.set(plot_guess = True, ymin = 1)
f.fit()
print(f)

A1, x0,x1, s1, g1, A2, A, A3, v, c= f.results[0]

##step = A2*Step(dx-x0, s1)
#Gua = A1*voigt(dx-x0, s1,g1)
#back = A*Quad(dx, a1,b1,c1)
#
#
#alloy_legend = ["Rod", "voigt", "Step Function", "Background"]
#s.plot.xy.data([dx,dx,dx,dx],\
#                  [dy,Gua,step,back],\
#                  xlabel = 'Bin',\
#                  ylabel = 'Counts',\
#                  label = alloy_legend,\
#                  legend = 'right')


#FIT WITH Exponential FUNCTION AS BACKGROUND
#def exponential(x,a,b): 
#    return np.exp(-(x-a)*b)
#    
#g = s.data.fitter()
#g.set_functions('E(x,a,b)', 'a,b', E= exponential)   
#g.set_data(xdata = dx, ydata = dy, eydata = y_error)
#
#g.set(xmin = 750, xmax = 1000)
#g.set(ymin = 1)
#
#g.set(a=800,b=1,  plot_guess = True, xlabel = 'Channel',
#      ylabel = 'Count')
#g.fit()
#print(g)
#a1,b1 = g.results[0]
#
#f = s.data.fitter()
#
#def fitfunction3(x, A1, x0, s, A2, A):
#    return A1*Gaussian(x-x0, s) + A2*Step(x-x0, s) + A*exponential(x,a1,b1)
#     
#f.set_functions('ft(x, A1, x0, s, A2,A)' , 'A1, x0, s, A2,A', ft=fitfunction3) 
#
#
#f.set_data(xdata = dx, ydata = dy, eydata = y_error)
#f.set(s = 50, A = 1)
#
#click_x1, click_y1 = f.ginput()[0]
#click_x2, click_y2 = f.ginput()[0]
#click_x3, click_y3 = f.ginput()[0]
#f.set(xmin = 500, xmax = 800)
#
#f.set(x0 = click_x1, A1= click_y1, A2 = click_y2 - click_y3,  plot_guess = True, xlabel = 'Channel',
#      ylabel = 'Count')
#f.set(plot_guess = True, ymin = 1)
#f.fit()
#print(f)

#A1, x0, s1, A2, A= f.results[0]
#
#step = A2*Step(dx-x0, s1)
#Gua = A1*Gaussian(dx-x0, s1)
#back = A*exponential(dx,b1)
##
#
#alloy_legend = ["Rod", "Gaussian", "Step Function", "Background"]
#s.plot.xy.data([dx,dx,dx,dx],\
#                  [dy,Gua,step,back],\
#                  xlabel = 'Bin',\
#                  ylabel = 'Counts',\
#                  label = alloy_legend,\
#                  legend = 'right')