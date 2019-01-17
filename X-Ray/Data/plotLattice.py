#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:05:23 2019

@author: vuongthaian
"""
import numpy as np
import spinmob as s


lam = 0.153*10**(-9)
hkl = np.sqrt(np.asarray([3, 4, 8, 11, 12]))
# Copy paste data from notes
theta2 = (np.asarray([[43.4224, 50.5387, 74.2585, 90.0771, 95.312],
		[43.7313, 50.9318, 74.8963, 90.923, 92.2],
		[44.0595, 51.3155, 75.501, 91.696, 92.12],
		[44.3206, 51.6249, 75.9962, 92.365, 93.25],
		[44.5913, 51.9418, 76.4947, 93.0779, 94.53]])/180) * np.pi
theta2_er = np.asarray([[0.0016, 0.0035, 0.006, 0.0084, 0.019],
		     [0.002, 0.0047, 0.0082, 0.013,  0.53],
		     [0.0024, 0.0057, 0.011,  0.016, 0.38],
		     [0.002, 0.0049, 0.0095,  0.014, 0.49], 
	         [0.0015, 0.0032, 0.0067, 0.009, 0.47]])
theta = theta2 / 2
theta_er = theta2_er / 2
sin = np.sin(theta)
sin_er = np.multiply(sin, theta_er, 1/np.tan(theta))


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


f1.set_data(xdata=hkl, ydata=sin[4], eydata=sin_er[4])
#f2.set_data(xdata=hkl, ydata=sin[1], eydata=sin_er[1])            
#f3.set_data(xdata=hkl, ydata=sin[2], eydata=sin_er[2])            
#f4.set_data(xdata=hkl, ydata=sin[3], eydata=sin_er[3])            
#f5.set_data(xdata=hkl, ydata=sin[4], eydata=sin_er[4]) 

f1.fit()

print(f1) 






 