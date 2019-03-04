#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:03:11 2019

@author: Elisa
"""

import numpy as np
import spinmob as s
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import peak_local_max
from skimage import data, img_as_float, io, util
from scipy import ndimage as ndi

#get dot positions for the 10 different images of single slit: 
    
    #IMAGE #1 
imgdots1 = io.imread("IMG_0739.jpg")
imdots1 = rgb2gray(imgdots1)
imdotsT1 = np.ndarray.transpose(imdots1)
avDot1 = np.empty(imdots1[0].size)
xdots1 = np.arange(0,imdots1[0].size,1)

for i in range(imdots1[0].size):
    avDot1[i] = np.average(imdotsT1[i])
    
    #IMAGE #2 
imgdots2 = io.imread("IMG_0741.jpg")
imdots2 = rgb2gray(imgdots2)
imdotsT2 = np.ndarray.transpose(imdots2)
avDot2 = np.empty(imdots2[0].size)
xdots2 = np.arange(0,imdots2[0].size,1)

for i in range(imdots2[0].size):
    avDot2[i] = np.average(imdotsT2[i])
    
    #IMAGE #3 
imgdots3 = io.imread("IMG_0742.jpg")
imdots3 = rgb2gray(imgdots3)
imdotsT3 = np.ndarray.transpose(imdots3)
avDot3 = np.empty(imdots3[0].size)
xdots3 = np.arange(0,imdots3[0].size,1)

for i in range(imdots3[0].size):
    avDot3[i] = np.average(imdotsT3[i])

    #IMAGE #4 
imgdots4 = io.imread("IMG_0743.jpg")
imdots4 = rgb2gray(imgdots4)
imdotsT4 = np.ndarray.transpose(imdots4)
avDot4 = np.empty(imdots4[0].size)
xdots4 = np.arange(0,imdots4[0].size,1)

for i in range(imdots4[0].size):
    avDot4[i] = np.average(imdotsT4[i]) 

    #IMAGE #5 
imgdots5 = io.imread("IMG_0744.jpg")
imdots5 = rgb2gray(imgdots5)
imdotsT5 = np.ndarray.transpose(imdots5)
avDot5 = np.empty(imdots5[0].size)
xdots5 = np.arange(0,imdots5[0].size,1)

for i in range(imdots5[0].size):
    avDot5[i] = np.average(imdotsT5[i]) 

    #IMAGE #6 
imgdots6 = io.imread("IMG_0745.jpg")
imdots6 = rgb2gray(imgdots6)
imdotsT6 = np.ndarray.transpose(imdots6)
avDot6 = np.empty(imdots6[0].size)
xdots6 = np.arange(0,imdots6[0].size,1)

for i in range(imdots6[0].size):
    avDot6[i] = np.average(imdotsT6[i]) 

    #IMAGE #7 
imgdots7 = io.imread("IMG_0747.jpg")
imdots7 = rgb2gray(imgdots7)
imdotsT7 = np.ndarray.transpose(imdots7)
avDot7 = np.empty(imdots7[0].size)
xdots7 = np.arange(0,imdots7[0].size,1)

for i in range(imdots7[0].size):
    avDot7[i] = np.average(imdotsT7[i]) 

    #IMAGE #8 
imgdots8 = io.imread("IMG_0748.jpg")
imdots8 = rgb2gray(imgdots8)
imdotsT8 = np.ndarray.transpose(imdots8)
avDot8 = np.empty(imdots8[0].size)
xdots8 = np.arange(0,imdots8[0].size,1)

for i in range(imdots8[0].size):
    avDot8[i] = np.average(imdotsT8[i]) 

    #IMAGE #9 
imgdots9 = io.imread("IMG_0749.jpg")
imdots9 = rgb2gray(imgdots9)
imdotsT9 = np.ndarray.transpose(imdots9)
avDot9 = np.empty(imdots9[0].size)
xdots9 = np.arange(0,imdots9[0].size,1)

for i in range(imdots9[0].size):
    avDot9[i] = np.average(imdotsT9[i]) 

    #IMAGE #10 
imgdots10 = io.imread("IMG_0750.jpg")
imdots10 = rgb2gray(imgdots10)
imdotsT10 = np.ndarray.transpose(imdots10)
avDot10 = np.empty(imdots10[0].size)
xdots10 = np.arange(0,imdots10[0].size,1)

for i in range(imdots10[0].size):
    avDot10[i] = np.average(imdotsT10[i]) 
    
""" Now, we have found the average intensity for each picture and its average pixel position. 
To be able to estimate the error we need to compare the maximum intensity of each AvDot array and fit those to a constant."""

max1 = np.max(avDot1)
max2 = np.max(avDot2)
max3 = np.max(avDot3)
max4 = np.max(avDot4)
max5 = np.max(avDot5)
max6 = np.max(avDot6)
max7 = np.max(avDot7)
max8 = np.max(avDot8)
max9 = np.max(avDot9)
max10 = np.max(avDot10)

#create an array of max and an array of photo # : 
tot_max = np.asarray([max1, max2, max3, max4, max5, max6, max7, max8, max9, max10])
photo_num = np.asarray([1,2,3,4,5,6,7,8,9,10])


#Now, use these max values to fit a constant: 
    
# Create a fitter object
f = s.data.fitter()
## Define the fit function (in this case, a constant) and fit parameters.
f.set_functions(f='a', p='a')
#
## Stick the data into the fitter object, and make an initial guess at the error bar
f.set_data(xdata=photo_num, ydata=tot_max, eydata=0.003)
#
## Fit!
f.fit()
#
## Show the results (see spinmob wiki for more details!)
print(f)


##Plot the different intensity vs pixel 
#fig, axs = plt.subplots(2, 2)
#
#axs[0,0].plot(xdots1,avDot1, 'r')
#axs[0,0].axes.set_xlim([100,5000])
#
#axs[0,1].plot(xdots2,avDot2, 'r')
#axs[0,1].axes.set_xlim([100,5000])
#
#axs[1,0].plot(xdots3,avDot3, 'r')
#axs[1,0].axes.set_xlim([100,5000])
#
#axs[1,1].plot(xdots4,avDot4, 'r')
#axs[1,1].axes.set_xlim([100,5000])

#plt.show()
