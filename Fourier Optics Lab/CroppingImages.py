#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 18:39:43 2019

@author: Elisa
"""


import numpy as np
import spinmob as s
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import peak_local_max
from skimage import data, img_as_float, io, util
from scipy import ndimage as ndi

#get dot positions
imgdots = io.imread("IMG_0750.jpg")[1500:3000,1750:4250]
imdots = rgb2gray(imgdots)
imdotsT = np.ndarray.transpose(imdots)
avDot = np.empty(imdots[0].size)
xdots = np.arange(0,imdots[0].size,1)
#for 0739: [1500:3000,1500:4000] 
#for 0741 : [1500:3000,1250:3750]
#for 0742: [1500:3000,1750:4250]
#for 0743: [1500:3000,1750:4250]
#for 0744: 1500:3000,2250:4750]
#for 0745: [1500:3000,1750:4250]
#for 0747: [1500:3000,1500:4000]
#for 0748: [1500:3000,1500:4000]
#for 0749: [1500:3000,1500:4000]
#for 0750: [1500:3000,1750:4250]
#optimal crop size: [1400:3100, 1250:4750]

for i in range(imdots[0].size): 
    avDot[i] = np.average(imdotsT[i])


fig, axs = plt.subplots(2, 2)

axs[0,0].imshow(imdots, cmap=plt.cm.gray)

axs[1,1].plot(xdots,avDot, 'r')
axs[1,1].axes.set_xlim([100,5000])



plt.show()
