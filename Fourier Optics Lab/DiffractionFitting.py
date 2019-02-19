# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 22:23:23 2019

@author: aorfi
"""

import numpy as np
import spinmob
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage import data, img_as_float, io

imgdots = io.imread("test.jpg")[2050:2150,1700:2800]
imgdots = io.imread("test.jpg")[700:1500][50:5500]
imdots = rgb2gray(imgdots)
imdotsT = np.ndarray.transpose(imdots)
avDot = np.empty(imdots[0].size)
xdots = np.arange(0,imdots[0].size,1)

for i in range(imdots[0].size):
    avDot[i] = np.average(imdotsT[i])
    
    
    
    
def Intensity_grating(w, s, x, N):
    focal = 0.3
    l = 0.0000006328
    #w = width of the slits 
    #s = separation of the slits 
    #N = number of slits 
    
    p = np.power(np.sinc(s*x/(l*focal)),2)
    q = np.power(np.sin(np.pi*N*s*x/(l*focal)),2)
    r = np.power(np.sin(np.pi*s*x/(l*focal)),2)
    
    return p*q/r

xdotsm = xdots*(0.00000429)
pattern = 0.01*Intensity_grating(0.0020, 0.01, (xdotsm-0.0116), 20)
plt.xlim([0.0001,0.03])

plt.plot(xdotsm,pattern)
plt.plot(xdotsm,avDot)
plt.show

#f1 = spinmob.data.fitter()
#f1.set_functions('A1*I(w,s,x,N)+c','A1, x1, w,  c=0', I = Intensity_grating)
#peakx = xdots[460:550]
#peaky = onDotLine[460:550]
#f1.set_data(peakx, peaky, 0.001)
#f1.set(w=6)
#click_x1, click_y1 = f1.ginput()[0]
##click_x2, click_y2 = f1.ginput()[0]
#f1.set(A1=click_y1, x1=click_x1, plot_guess = True, 
#      xlabel='Relative Brightness',
#      ylabel='Pixles')
#f1.fit()
#print(f1)

