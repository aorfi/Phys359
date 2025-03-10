#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 21:00:19 2019

@author: vuongthaian
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

def SingleSlitInt(x,w,I):
    const = np.pi*w/(focal*wavelength)
    var = const*x
    return I*(np.power(np.sin(var),2)/np.power(var,2))

#def MultiSlit(x,w,I,N):
#    const1 = np.pi*w/(focal*wavelength)
#    const2 = np.pi*dark/(focal*wavelength)
#    var1 = const1*x
#    var2 = const2*x
#    return I*np.power(np.sin(var1)/var1,2)*np.power(np.sin(N*var1)/(N*np.sin(var1)),2)


#in diffraction fitting : xdotsm = xdots*(0.00000429)

            #FOR : EQ1407

#get intensity data from the image; 
imgdots1 = io.imread("IMG_0711.jpg")
imdots1 = rgb2gray(imgdots1)
imdotsT1 = np.ndarray.transpose(imdots1)
avDot1 = np.empty(imdots1[0].size)

for i in range(imdots1[0].size):
    avDot1[i] = np.average(imdotsT1[i])


#we need to translate the data so that the maximum intensity of the image lies
#on y axis: 
max_intensity = np.max(avDot1)
pos = avDot1.tolist().index(max_intensity)#gives an index
total = avDot1.size #total number of points 
beg = -1*pos
end = total - pos
xdots1 = np.arange(beg,end,1)
xdotsm1 = xdots1*(0.00000429) #go to measure of distance not pixel count\

#for this grating the width of a slit is: 
width = 0.0625 *(1/np.power(10,2)) #in m 
y_singleSlit1 = SingleSlitInt(xdotsm1,width,(max_intensity-np.min(avDot1)))
#y_multiSlit = MultiSlit(xdotsm1,width,(max_intensity-np.min(avDot1)), N)
#plt.plot(xdotsm1,y_singleSlit)
#plt.plot(xdotsm1,(avDot1-np.min(avDot1)))
#plt.plot(xdotsm1,y_multiSlit)


y1 = np.divide(avDot1-np.min(avDot1), y_singleSlit1)
Y1_min = np.ones(xdotsm1.size)*5*np.power(10,6)

plt.plot(xdotsm1, y1)
plt.plot(xdotsm1, Y1_min)

plt.show()

#find a value of y beyond which only the delta functions cross it. 
#this is Y1_min 
index1 = np.transpose(np.where(y1>Y1_min)) #gives the array of indices where the condition is met 
print(index1)
#to find the distance between the peaks: 
dist1 = xdotsm1[index1[2]]-xdotsm1[index1[1]]
print(dist1/2)

#calculating slit separation: 
dark = 0.0375 *(1/np.power(10,2)) #in m 
separation = width/2 + dark
print(separation)


