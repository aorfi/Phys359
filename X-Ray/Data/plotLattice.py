#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:05:23 2019

@author: vuongthaian
"""
import numpy as np
import spinmob as s

fileName = ['Cu100-Sheet1.csv', 'Cu75Ni25-Sheet1.csv', 'Cu50Ni50-Sheet1.csv',
            'Cu25Ni75-Sheet1.csv', 'Ni100-Sheet1.csv']

lam = 0.153*10**(-9)
hkl = np.sqrt(np.asarray([3, 4, 8, 11]))
# Copy paste data from notes

w1theta2 = np.array([]);
w2theta2 = np.array([]);
w1theta2_er = np.array([]);
w2theta2_er = np.array([]);

for i in range(0,5):
    a = s.data.load(fileName[i])
    w1theta2 = np.append(w1theta2, a[0], axis = 0)
    w1theta2_er = np.append(w1theta2_er, a[1], axis = 0)
    w2theta2 = np.append(w2theta2, a[2], axis = 0)
    w2theta2_er = np.append(w2theta2_er, a[3], axis = 0)
    
w1theta = ((w1theta2/180) * np.pi) / 2;
w1theta_er = ((w1theta2_er/180) * np.pi) / 2;
w2theta = ((w2theta2/180) * np.pi) / 2
w2theta_er = ((w2theta2_er/180) * np.pi) / 2;
    
sin1 = np.sin(w1theta)
sin1_er = np.multiply(w1theta_er, np.cos(w1theta))
sin2 = np.sin(w2theta)
sin2_er = np.multiply(w2theta_er, np.cos(w2theta))


# Create a fitter object
f1 = s.data.fitter()
f2 = s.data.fitter()


# Define the fit functions (in this case, the sum of two Lorentzians) 
# and floating parameters.

f1.set_functions('a*x+b', 'a', 'b')
f2.set_functions('c*x+m', 'c', 'm')



f1.set_data(xdata=hkl, ydata=sin1[0], eydata=sin1_er[0])
f2.set.data(xdata=hkl, ydata=sin2[0], eydata=sin2_er[0])


f1.set(xlabel = 'Square-root sum hkl', ylabel = 'sin'r'$\theta$')
f2.set(xlabel = 'Square-root sum hkl', ylabel = 'sin'r'$\theta$')

f1.fit()
f2.fit()

print(f1) 
print(f2)






 