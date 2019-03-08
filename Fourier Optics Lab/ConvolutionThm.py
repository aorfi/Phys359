#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 08:57:36 2019

@author: Elisa
"""

import numpy as np
import spinmob as s
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import peak_local_max
from skimage import data, img_as_float, io, util
from scipy import ndimage as ndi

#define a new function: the FT^2 of a single slit aperture function 
focal = 0.3
wavelength = 0.0000006328

def SingleSlitInt(x,w): 
    nu = x/(focal*wavelength)
    temp = nu*w
    return np.power(w,2)*np.sinc(temp)*np.sinc(temp)

#in diffraction fitting : xdotsm = xdots*(0.00000429)

            #FOR : EQ1408

#get intensity data from the image; 
imgdots1 = io.imread("IMG_0700.jpg")
imdots1 = rgb2gray(imgdots1)
imdotsT1 = np.ndarray.transpose(imdots1)
avDot1 = np.empty(imdots1[0].size)
xdots1 = np.arange(0,imdots1[0].size,1)
xdotsm1 = xdots1*(0.00000429) #go to measure of distance not pixel count

#for this grating the width of a slit is: 
width = 0.025*(1/np.power(10,3)) #in m 
y_singleSlit = SingleSlitInt(xdotsm1,width)
plt.plot(xdotsm1,y_singleSlit)
plt.plot(xdotsm1,avDot1)
plt.show()



