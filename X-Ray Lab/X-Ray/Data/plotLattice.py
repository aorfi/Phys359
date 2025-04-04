#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 17:05:23 2019

@author: vuongthaian
"""
import numpy as np
import spinmob as s

isCu = False;

if (isCu == True):
    hkl = np.sqrt(np.asarray([3, 4, 8, 11, 12]))
    final = 5;
    fileName = ['Cu100-Sheet1.csv', 'Cu75Ni25-Sheet1.csv', 'Cu50Ni50-Sheet1.csv',
                'Cu25Ni75-Sheet1.csv', 'Ni100-Sheet1.csv']
else:
#    hkl = np.sqrt(np.asarray([3, 4, 8, 11, 12, 16, 19, 20, 24, 27]))
#    hkl = np.sqrt(np.asarray([3, 8, 11, 16, 19, 24, 27, 32, 35, 40, 43]))
#    hkl = np.sqrt(np.asarray([3, 4, 8, 11, 12, 16]))
#    hkl = np.sqrt(np.asarray([3, 4, 8, 11, 12, 16, 19, 20, 24]))
#    hkl = np.sqrt(np.asarray([4.92,   5.376 ,   9.846,
#                              10.30, 15.22 ,  18.99,  20.113,  24.6,
#                              25.04,  28.827,  34.856]))
    hkl = np.sqrt(np.asarray([3, 4, 5, 8, 11, 12]))
    hkl = np.sqrt(np.asarray([1, 2, 3, 4, 5, 6, 8, 11, 12]))
    final = 1; 
    fileName = ['Cu3Au-B-Sheet1.csv']

    

lam1 = 0.15443*10**(-9)
lam2 = 0.15405*10**(-9)
lam = (1/2)*(lam1 + lam2)

coeff = [];
coeff_er = [];
# Copy paste data from notes

#w1theta2 = np.zeros((5,1));
#w2theta2 = np.zeros((5,1));
#w1theta2_er = np.zeros((5,1));
#w2theta2_er = np.zeros((5,1));

w1theta2 = [];
w2theta2 = [];
w1theta2_er = [];
w2theta2_er = [];

for i in range(0,final):
    a = s.data.load(fileName[i])
#    b0 = np.asarray(a[0])
#    b1 = np.asarray(a[1])
#    b2 = np.asarray(a[2])
#    b3 = np.asarray(a[3])
    w1theta2.append(a[0])
    w1theta2_er.append(a[1])
    w2theta2.append(a[2])
    w2theta2_er.append(a[3])
    
    
w1theta = ((np.asarray(w1theta2)/180) * np.pi) / 2;
w1theta_er = ((np.asarray(w1theta2_er)/180) * np.pi) / 2;
w2theta = ((np.asarray(w2theta2)/180) * np.pi) / 2
w2theta_er = ((np.asarray(w2theta2_er)/180) * np.pi) / 2;

mean_theta = (1/2) * (w1theta + w2theta)
mean_theta_er = np.sqrt(w1theta_er**2 + w2theta_er**2)
    
sin1 = np.sin(w1theta)
sin1_er = np.multiply(w1theta_er, np.cos(w1theta))
sin2 = np.sin(w2theta)
sin2_er = np.multiply(w2theta_er, np.cos(w2theta))

sin_mean = np.sin(mean_theta);
sin_mean_er = np.multiply(mean_theta_er, np.cos(sin_mean));

ratio = sin_mean**2/(sin_mean[0]**2)

for i in range(0,final):
    # Create a fitter object
    f = s.data.fitter()
    #f2 = s.data.fitter()
    
    # Define the fit functions (in this case, the sum of two Lorentzians) 
    # and floating parameters.
    
    
    
    f.set_functions('a*x+b', 'a, b')
    #f2.set_functions('c*x+m', 'c, m')
    
    f.set(b = 0.9, a = 0.1)
    #f2.set(m = 0, c = 0.2)
    
    f.set_data(xdata=hkl, ydata=sin_mean[i], eydata=sin_mean_er[i])
    #f2.set_data(xdata=hkl, ydata=sin2[0], eydata=sin2_er[0])
    
    
    f.set(xlabel = r'$\sqrt{h^2+k^2+l^2}$', ylabel = 'sin'r'$\theta$',
           plot_guess = False)
    #f2.set(xlabel = 'Square-root sum hkl', ylabel = 'sin'r'$\theta$',
    #       plot_guess = False)
    
    f.fit()
    #f2.fit()
    
    print(f) 
    #print(f2)
    a = f.results
    coeff.append(a[0][0])
    coeff_er.append(np.sqrt(a[1][0][0]))
    
lattice = (lam/(2*np.asarray(coeff)))
lattice_er = (lam/2) * (np.asarray(coeff_er)/(np.asarray(coeff)**2))
#
#
##PLOT LATTICE VS CONCENTRATION
#con = [100, 75, 50, 25, 0]
#s.plot.xy.data(con, lattice, eydata = lattice_er,
#               linestyle = '',
#               marker = '.',
#               color = 'r',
#               xlabel = 'Copper Concentration %',
#               ylabel = 'Lattice Constant ' r'$\AA$')
#
#f1 = s.data.fitter()
#f1.set_functions('a*x+b', 'a, b')
#f1.set(b = 0.9, a = 0.1)
#f1.set_data(xdata=con, ydata=lattice, eydata=lattice_er) 
#f1.set(xlabel = 'Copper Concentration %',
#       ylabel = 'Lattice Constant ' r'$\AA$',
#       plot_guess = False)
#f1.fit()
#print(f1)
#   







 