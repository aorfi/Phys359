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
dark = 0.0000375

#def SingleSlitInt(x,w): 
#    nu = x/(focal*wavelength)
#    temp = nu*w
#    return np.power(w,2)*np.sinc(temp)*np.sinc(temp)

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

            #FOR : EQ1408

#get intensity data from the image; 
imgdots1 = io.imread("IMG_0718.jpg")
width = 0.1*(1/np.power(10,2)) #in m 
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

N = 16
y_singleSlit = SingleSlitInt(xdotsm1,width,(max_intensity-np.min(avDot1)))
#y_multiSlit = MultiSlit(xdotsm1,width,(max_intensity-np.min(avDot1)), N)
imdata = (avDot1-np.min(avDot1))
rat = imdata/y_singleSlit

xmax = np.empty(2) 
ymax = np.empty(2) 
a = 2300
b = 2400
c = 2400
d = 2500
ymax[0] = np.amin(imdata[a:b])
xmax[0] = np.argmin(imdata[a:b]) - pos+a 
ymax[1] = np.amin(imdata[c:d])
xmax[1] = np.argmin(imdata[c:d]) - pos+c

plt.plot(xdotsm1,y_singleSlit)
plt.plot(xdotsm1,imdata)
#plt.plot(xdotsm1,rat)
plt.plot(xmax*(0.00000429),ymax,'ro')
#plt.plot(xdotsm1,y_multiSlit)
plt.show()



