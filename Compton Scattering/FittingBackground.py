# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:51:09 2019

@author: aorfi
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
    
#OFFSET 
#these are 3 functions that affect the gaussian curve that we are fitting for! 
#with our data, we want to fit the sum of all 3 + offset 
#check with the website written down: https://www.nndc.bnl.gov/nudat2/chartNuc.jsp 
#for whether or not we have more than 1 peak that we should be fitting (generally, start fitting 1 peak and see)

#gaussian and step should have the same x_0 and the same sigma 

#chose data: 
rod = s.data.load('ENal_25deg.dat')
norod = s.data.load('ENnorod_25deg.dat')
y_error = norod[1]**(1/2)

#alloy_legend = ["Rod", "No Rod"] 
#s.plot.xy.data([rod[0],norod[0]],\
#                  [rod[1],norod[1]],\
#                  xlabel = 'Bin',\
#                  ylabel = 'Counts',\
#                  label = alloy_legend,\
#                  legend = 'right')

#FIT FOR BACKGROUND LINE FIRST: 
h = s.data.fitter() 
h.set_functions('L(x,m,b)', 'm,b', L = Line)

h.set_data(xdata=norod[0], ydata=norod[1], eydata = y_error)
h.set(xmin = 1000, xmax = 1700, ymin = 1)

click_x2, click_y2 = h.ginput()[0]
click_x3, click_y3 = h.ginput()[0]
h.set(b =1 , m = (click_y2-click_y3)/(click_x2-click_x3) , plot_guess = True, xlabel = "Energy", ylabel = 'Count' )
h.fit()
print(h)

Bm, Bb = h.results[0] 


f = s.data.fitter()

f.set_functions('A1*G(x-x0, s) + A2*S(x-x0, s) + L(x,m,b)', 'A1, x0, s, A2', G= Gaussian, S = Step, L=Line, m=Bm, b = Bb) 
#f.set_functions('A1*G(x-x0, s) + A2*S(x-x0, s)', 'A1,x0,s,A2', G = Gaussian, S = Step)


f.set_data(xdata = norod[0], ydata = norod[1], eydata = y_error)
f.set(s = 15)

click_x1, click_y1 = f.ginput()[0]
click_x2, click_y2 = f.ginput()[0]
click_x3, click_y3 = f.ginput()[0]

f.set(xmin=click_x1-100, xmax=click_x1+100)

f.set(x0 = click_x1, A1= click_y1, A2 = click_y3 - click_y2,  plot_guess = False, xlabel = 'Energy keV',
      ylabel = 'Count')
f.set(plot_guess = False, ymin = 2)
f.fit()
print(f)


BA1, Bx0, Bs, BA2 = f.results[0]
x_axis = norod[0]
l = Line(x_axis,Bm,Bb)
gaus = BA1*Gaussian(x_axis-Bx0, Bs) 
st = BA2*Step(x_axis-Bx0, Bs)

#s.plot.xy.data([x_axis,x_axis,x_axis,x_axis],\
#                  [norod[1],l,st,gaus],\
#                  xlabel = 'Bin',\
#                  ylabel = 'Counts')




g = s.data.fitter()
g.set_functions('A1*G(x-x0, s) + A2*S(x-x0, s) + A3*(bA1*G(x-bx0, bs) + bA2*S(x-bx0, bs) + L(x,bm,bb)) ', 'A1, x0, s, A2, A3', G= Gaussian, S = Step, L=Line,bA1=BA1, bs=Bs, bx0=Bx0, bA2=BA2, bm=Bm, bb=Bb) 

y_error = rod[1]**(1/2)

g.set_data(xdata = rod[0], ydata = rod[1], eydata = y_error)
g.set(s = 15, A3=1)
g.set(xmin=400, xmax=700)

click_x1, click_y1 = g.ginput()[0]
click_x2, click_y2 = g.ginput()[0]
click_x3, click_y3 = g.ginput()[0]



g.set(x0 = click_x1, A1= click_y1, A2 = click_y2 - click_y1, plot_guess = False, xlabel = 'Channel',
      ylabel = 'Count')
g.set(plot_guess = False, ymin = 2)
g.fit()
print(g)

A1, x0, s1, A2, A3= g.results[0]
x = rod[0]
step = A2*Step(x-x0, s1)
Gua = A1*Gaussian(x-x0, s1)
back = A3*(BA1*Gaussian(x-Bx0, Bs) + BA2*Step(x-Bx0, Bs) + Line(x,Bm,Bb))


alloy_legend = ["Rod", "background", "Step Function", "Gaussian"]
s.plot.xy.data([x,x,x,x],\
                  [rod[1],back,step,Gua],\
                  xlabel = 'Bin',\
                  ylabel = 'Counts',\
                  label = alloy_legend,\
                  legend = 'right')


#f(plot_all_data = True)

