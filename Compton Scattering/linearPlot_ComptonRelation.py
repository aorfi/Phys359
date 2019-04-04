#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 29 13:57:25 2019

@author: Elisa
"""

import spinmob as s
import numpy as np
import matplotlib.pyplot as plt
from tempfile import TemporaryFile 

#start with the arrays of data: 

ene = np.asarray([583.65, 555.7, 532.12, 504.52 ]) #[20, 25deg, 30deg,35deg, 40]
err_ene = np.asarray([0.26, 0.32, 0.34, 0.36])

angle = np.asarray([25,30,35,40])*np.pi/180
err_angle = np.asarray([0.5,0.5,0.5,0.5])*np.pi/180


n = ene.size

#CODE FOR PROPAGATION OF ERRORS DUE TO BIN TRANSLATION
##translate them by Xbin numbers, where X is the number of bins obtained from trueAngle analysis 
#Xbin = (371.29-368.14)/2 
#bin_translation = Xbin*np.ones(n)
#
#err_bintranslation = np.ones(n)*np.sqrt(pow(0.54,2)+pow(0.16,2))
#
##correct channel: 
#channel = np.subtract(c, bin_translation) #subtracting! 
#err_ch = np.sqrt(np.add(pow(err_bintranslation,2),pow(err_c,2)))
#
##now define m and b, fit parameters of the calibration: 
#m = 0.556622*np.ones(n) 
#err_m = 0.00028* np.ones(n) 
#b = -4.685* np.ones(n) 
#err_b = 0.056 *np.ones(n) 
#
##find error that comes from subtracting channel - b: 
#err_ch_b = np.sqrt(np.add(err_ch**2,err_b**2))
#ch_b = np.subtract(channel, b)
#
##now find energy and the error on energy: 
#
#ene = np.divide(ch_b,m)
#alpha = pow(np.divide(err_ch_b, ch_b),2)
#beta = pow(np.divide(err_m, m),2)
#err_ene = ene*np.sqrt(alpha+beta)


#original energy of incoming ray: 
e_0 = np.ones(n)*661.657
h = pow(10, -34)*6.626070040
c = 299792458

#finding delta_lambda/(hc): 
inverse_ene = np.subtract(np.divide(1,ene), np.divide(1,e_0))
#finding error on delta lambda: 

inverse_ene_err = (err_ene) * np.power(np.divide(1,ene),2) 
    
#the x axis will be (1 - cos(theta)): 
x_axis = 1-np.cos(angle)
x_err= np.abs(np.multiply(err_angle,np.sin(angle)))


#theoretical slope of this line: 1 / (electron rest energy)
m_theo = 0.001931 #taken from that link #This is in KeV
theoretical_line = m_theo * x_axis
#plot: 

#plt.errorbar(x_axis, delta_lambda, yerr = delta_lambda_err, xerr = x_err, fmt='.')
plt.plot(x_axis,theoretical_line)
plt.plot(x_axis, inverse_ene, marker='.')
plt.show()

#print(delta_lambda_err)
#now perform a fit 
f = s.data.fitter()
f.set_functions('m*x + b ', 'm, b')
f.set_data(ydata = x_axis, xdata = inverse_ene, eydata = x_err)
f.set(m = 1/m_theo)
##
##### CLICK
f.set(plot_guess = False, ylabel = '1-cos'r'($\theta$)',
     xlabel = '(1/E1) - (1/E2)')
f.fit()
print(f)


