# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:58:35 2019

@author: aorfi
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import peak_local_max
from skimage import data, img_as_float, io, util
from scipy import ndimage as ndi

#First get scale of the image
img = io.imread("test.jpg")[700:1400, 2000:4000]
image = rgb2gray(img)
#image = img_grey[1200:1500]
im = img_as_float(image)
y = np.empty(im[0].size)
linePosition = 300 #defines line guess from photo
y.fill(linePosition) #defines line 
x = np.arange(0,im[0].size,1)
onLine = 1-im[linePosition]

plt.subplot(2,1,1)
plt.imshow(im, cmap=plt.cm.gray)
plt.plot(x,y)


plt.subplot(2,1,2)
plt.plot(x,onLine, 'b')


plt.show()

#
#image_max = ndi.maximum_filter(im, size=150, mode='constant') #finds local max
#coordinates = peak_local_max(im, min_distance=150)




#fig, axes = plt.subplots(1, 3, figsize=(8, 3), sharex=True, sharey=True)
#ax = axes.ravel()
#ax[0].imshow(im, cmap=plt.cm.gray)
#ax[0].set_title('Original')
#
#ax[1].imshow(image_max, cmap=plt.cm.gray)
#ax[1].set_title('Maximum filter')
#
#ax[2].imshow(im, cmap=plt.cm.gray)
#ax[2].autoscale(False)
#ax[2].plot(coordinates[:, 1], coordinates[:, 0], 'r.')
#ax[2].set_title('Peak local max')
#
#print(coordinates)
#
#
#fig.tight_layout()
#plt.show()




