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
from scipy.special import erfc
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

def skew_gaus(x,sigma, beta):
    return exp((x)/beta)*erfc((x)/((2**0.5)*sigma) + (sigma)/((2**0.5)*beta))
#sigma is the standard dev of the gaussian 
#beta is a new parameter we are fitting which determines the skewedness of the gaussian. 
#the skewed gaussian should have x-x0 like the other gaussian 
    
#OFFSET 
#these are 3 functions that affect the gaussian curve that we are fitting for! 
#with our data, we want to fit the sum of all 3 + offset 
#check with the website written down: https://www.nndc.bnl.gov/nudat2/chartNuc.jsp 
#for whether or not we have more than 1 peak that we should be fitting (generally, start fitting 1 peak and see)

#gaussian and step should have the same x_0 and the same sigma 

#
data = s.data.load('2brickEFF.dat')
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

g.set(xmin = 750, xmax = 1700)
g.set(ymin = 0.01)

g.set(b=0.1,a=0.1,c=1,  plot_guess = True, xlabel = 'Channel',
      ylabel = 'Count')
g.fit()
print(g)
a1,b1,c1 = g.results[0]
#
f = s.data.fitter()

#def skew_gaus(x,sigma, beta):
#    return exp((x)/beta)*erfc((x)/((2**0.5)*sigma) + (sigma)/((2**0.5)*beta))
#sigma is the standard dev of the gaussian 
#beta is a new parameter we are fitting which determines the skewedness of the gaussian. 
#the skewed gaussian should have x-x0 like the other gaussian 


def fitfunction2(x, A1, x0, s, A2, A3, beta, A4,C):
    return A1*Gaussian(x-x0, s) + A2*Step(x-x0, s) + A3*skew_gaus(x-x0,s, beta) + A4*Quad(x,a1,b1,c1)+C
     
f.set_functions('ft(x, A1, x0, s, A2, A3, beta, A4,C)' , ' A1, x0, s, A2, A3, beta, A4,C', ft=fitfunction2) 


f.set_data(xdata = dx, ydata = dy, eydata = y_error)
f.set(s = 30, beta = 10 , A3 = 700, A4 = 1, C=1)

click_x1, click_y1 = f.ginput()[0]
click_x2, click_y2 = f.ginput()[0]
click_x3, click_y3 = f.ginput()[0]
f.set(xmin = 500, xmax = 725)

f.set(x0 = click_x1, A1= click_y1 ,A2 = click_y2 - click_y3 - Quad(click_x2,a1,b1,c1), plot_guess = True, xlabel = 'Channel',
      ylabel = 'Count') 
f.set(plot_guess = True, ymin = 1)
f.fit()
print(f)

A1, x0, s1, A2, A3, beta, A4,C = f.results[0]

step = A2*Step(dx-x0, s1)
Gua = A1*Gaussian(dx-x0, s1)
back = A4*Quad(dx, a1,b1,c1)
skew = A3*skew_gaus(dx-x0,s1,beta)
fit = A1*Gaussian(dx-x0, s1) + A2*Step(dx-x0, s1) + A3*skew_gaus(dx-x0,s1, beta) + A4*Quad(dx,a1,b1,c1)+C
#
#
alloy_legend = ["Rod", "Gaussian", "Step Function", "Skewed Gaussian", "Background", "Fit"]
s.plot.xy.data([dx,dx,dx,dx,dx,dx],\
                  [dy,Gua,step,skew,back,fit],\
                  xlabel = 'Energy',\
                  ylabel = 'Counts',\
                  label = alloy_legend,\
                  legend = 'right')


for i in range(dx.size):
    if dx[i]-x0 <1:
        index = i
    


#TRYING AGAIN WITH QUADRATIC BACKGROUND BUT THIS TIME FITTING SKEWED GAUSSIAN FIRST 

#g = s.data.fitter()
#g.set_functions('Q(x,a,b,c)', 'a,b,c', Q= Quad)   
#g.set_data(xdata = dx, ydata = dy, eydata = y_error)

#g.set(xmin = 750, xmax = 1000)
#g.set(ymin = 1)
#
#g.set(b=1,a=1,c=1,  plot_guess = True, xlabel = 'Energy',
#      ylabel = 'Count')
#g.fit()
#print(g)
#a1,b1,c1 = g.results[0]
##
#
#h = s.data.fitter() 
#h.set_functions('A* Sk(x-x1,sig,beta)', 'A,x1,sig,beta', Sk = skew_gaus)   
#h.set_data(xdata = dx, ydata = dy, eydata = y_error)
#h.set(xmin = 300, xmax = 500)
#h.set(ymin = 1)
#click_x1, click_y1 = h.ginput()[0]
#
#
#h.set(x1 = click_x1, A = click_y1, sig = 15, beta = 300,plot_guess = True, xlabel = 'Energy',
#      ylabel = 'Count')
#h.fit()
#print(h)
#A,x1,sig1,beta1= h.results[0]

#f = s.data.fitter()
#
#
#def fitfunction2(x, A1, x0, s, A2, A4):
#    return A1*Gaussian(x-x0, s) + A2*Step(x-x0, s) + A*skew_gaus(x-x1,sig1, beta1) + A4*Quad(x,a1,b1,c1)
#     
#f.set_functions('ft(x, A1, x0, s, A2, A4)' , ' A1, x0, s, A2, A4', ft=fitfunction2) 
#
#
#f.set_data(xdata = dx, ydata = dy, eydata = y_error)
#f.set(s = 15, A4 = 1)
#
#click_x1, click_y1 = f.ginput()[0]
#click_x2, click_y2 = f.ginput()[0]
#click_x3, click_y3 = f.ginput()[0]
#f.set(xmin = 500, xmax = 800)
#
#f.set(x0 = click_x1, A1= click_y1 ,A2 = click_y2 - click_y3, plot_guess = True, xlabel = 'Channel',
#      ylabel = 'Count') 
#f.set(plot_guess = True, ymin = 1)
#f.fit()
#print(f)
#
#A1, x0, s1, A2, A4 = f.results[0]
#
#step = A2*Step(dx-x0, s1)
#Gua = A1*Gaussian(dx-x0, s1)
#back = A4*Quad(dx, a1,b1,c1)
#skew = A*skew_gaus(dx-x1,sig1,beta1)
###
##
#alloy_legend = ["Rod", "Gaussian", "Step Function", "Skewed Gaussian", "Background"]
#s.plot.xy.data([dx,dx,dx,dx,dx],\
#                  [dy,Gua,step,skew,back],\
#                  xlabel = 'Energy',\
#                  ylabel = 'Counts',\
#                  label = alloy_legend,\
#                  legend = 'right')