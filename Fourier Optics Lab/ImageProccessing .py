# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:58:35 2019

@author: aorfi
"""
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import peak_local_max
from skimage import data, img_as_float
from scipy import ndimage as ndi

img = io.imread("test.jpg")[1100:1500]
image = rgb2gray(img)
#image = img_grey[1200:1500]
im = img_as_float(image)
image_max = ndi.maximum_filter(im, size=150, mode='constant')
coordinates = peak_local_max(im, min_distance=150)
averages = np.zeros(img.size)
for x in xrange(0,coordinates.size):
    averages[i] = coordinates[i][0]

line = np.average(averages)
x = np.arange(0,img.size)
y = np.full(img.size, line)


fig, axes = plt.subplots(1, 3, figsize=(8, 3), sharex=True, sharey=True)
ax = axes.ravel()
ax[0].imshow(im, cmap=plt.cm.gray)
ax[0].set_title('Original')

ax[1].imshow(image_max, cmap=plt.cm.gray)
ax[1].set_title('Maximum filter')

ax[2].imshow(im, cmap=plt.cm.gray)
ax[2].autoscale(False)
ax[2].plot(coordinates[:, 1], coordinates[:, 0], 'r.')
ax[2].plot(x, y, 'b')
ax[2].set_title('Peak local max')

print(coordinates)
print(line)

fig.tight_layout()

plt.show()




