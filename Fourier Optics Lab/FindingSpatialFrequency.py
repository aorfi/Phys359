#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 16:32:07 2019

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
focal = 0.3
wavelength = 0.0000006328
    #IMAGE #1 : EQ1407
imgdots1 = io.imread("IMG_0700.jpg")
imdots1 = rgb2gray(imgdots1)
imdotsT1 = np.ndarray.transpose(imdots1)
avDot1 = np.empty(imdots1[0].size)
xdots1 = np.arange(0,imdots1[0].size,1)
xdotsm1 = xdots1*(0.00000429)

for i in range(imdots1[0].size):
    avDot1[i] = np.average(imdotsT1[i])

pos = avDot1.tolist().index(np.max(avDot1))#gives index of max intensity 
x_prime = xdotsm1[pos]

fundamental_frequency = x_prime/(focal*wavelength)
print(fundamental_frequency)


    