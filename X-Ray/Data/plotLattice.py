#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:05:23 2019

@author: vuongthaian
"""
import numpy as np
import spinmob as s


lam = 0.153*10**(-9)
hkl = np.sqrt(np.asarray([3, 4, 8, 11]))
# Copy paste data from notes
theta2 = (np.asarray([[43.422488124126247,
  50.538879958268062,
  74.259957909951481,
  90.07906902301157],
 [43.731513813127584,
  50.93162915710807,
  74.894145225289606,
  90.920955822351942],
 [44.059556042591701,
  51.316208132209752,
  75.503051524996479,
  91.701948883496499],
 [44.320566950231033,
  51.625194867517934,
  75.998388989826196,
  92.367161098213188],
 [44.591298799325209,
  51.941634740501044,
  76.494975314369071,
  93.072461981797943]])/180) * np.pi
theta2_er = np.asarray([[0.001556028223193572,
  0.0035317505691696205,
  0.0060474975805354632,
  0.0085906508184917067],
 [0.0019869760545405553,
  0.0046559388825345212,
  0.0081380776912848181,
  0.012305670392146547],
 [0.0024472275040163267,
  0.0056652269453274801,
  0.010894057917604137,
  0.016490399991613565],
 [0.0020355315963667396,
  0.0049249250394207984,
  0.0096466291926179462,
  0.015478439628497365],
 [0.0015131878911078982,
  0.0031993763575625276,
  0.0066257397383578196,
  0.0090638346332873668]])

theta = theta2 / 2
theta_er = theta2_er / 2
sin = np.sin(theta)
sin_er = np.multiply(theta_er, np.cos(theta))


# Create a fitter object
f1 = s.data.fitter()
f2 = s.data.fitter()
f3 = s.data.fitter()
f4 = s.data.fitter()
f5 = s.data.fitter()

# Define the fit functions (in this case, the sum of two Lorentzians) 
# and floating parameters.

f1.set_functions('a*x+b', 'a, b')
#f2.set_functions('A2*V(x-x2,s2,a2)', 'A2, x2, s2, a2', V= voigt)
#f3.set_functions('A3*V(x-x3,s3,a3)', 'A3, x3, s3, a3', V= voigt)
#f4.set_functions('A4*V(x-x4,s4,a4)', 'A4, x4, s4, a4', V= voigt)
#f5.set_functions('A5*V(x-x5,s5,a5)', 'A5, x5, s5, a5', V= voigt)


f1.set_data(xdata=hkl, ydata=sin[0], eydata=sin_er[0])
#f2.set_data(xdata=hkl, ydata=sin[1], eydata=sin_er[1])            
#f3.set_data(xdata=hkl, ydata=sin[2], eydata=sin_er[2])            
#f4.set_data(xdata=hkl, ydata=sin[3], eydata=sin_er[3])            
#f5.set_data(xdata=hkl, ydata=sin[4], eydata=sin_er[4]) 
f1.set(xlabel = 'Square-root sum hkl', ylabel = 'sin'r'$\theta$')

f1.fit()

print(f1) 






 