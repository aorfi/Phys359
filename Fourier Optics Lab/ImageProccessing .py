# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:58:35 2019

@author: aorfi
"""
import numpy as np
import spinmob
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.feature import peak_local_max
from skimage import data, img_as_float, io, util
from scipy import ndimage as ndi

#First get scale of the image
img = io.imread("test.jpg")[700:1400, 2000:4000]
image = rgb2gray(img)
im = img_as_float(image)
y = np.empty(im[0].size)
linePosition = 300 #defines line guess from photo
y.fill(linePosition) #defines line 
x = np.arange(0,im[0].size,1)
onLine = 1-im[linePosition]

#get dot positions
imgdots = io.imread("test.jpg")[2050:2150,1700:2800]
imagedots = rgb2gray(imgdots)
imdots = img_as_float(imagedots)
ydots = np.empty(imdots[0].size)
linePosition = 50 #defines line guess from photo
ydots.fill(linePosition) #defines line 
xdots = np.arange(0,imdots[0].size,1)
onDotLine = imdots[linePosition]

fig, axs = plt.subplots(2, 2)


axs[0,0].imshow(im, cmap=plt.cm.gray)
axs[0,0].plot(x,y)

axs[1,0].plot(x,onLine, 'b')

axs[0,1].imshow(imdots, cmap=plt.cm.gray)
axs[0,1].plot(xdots,ydots)

axs[1,1].plot(xdots,onDotLine, 'b')


plt.show()


#peak fitting of the graph paper
def guassian(x,x1,w):
    return np.exp(-((x-x1)**2)/(2*w**2))

f1 = spinmob.data.fitter()
f1.set_functions('a*G(x,x1,w)+c', 
                'a, x1, w, c', G=guassian)
peakx = x[465:510]
peaky = onLine[465:510]
f1.set_data(peakx, peaky, 0.01)
f1.set(c=0.89, w=5)
click_x1, click_y1 = f1.ginput()[0]
f1.set(a=0.05, x1=click_x1, plot_guess = True, 
      xlabel='Relative Brightness',
      ylabel='Pixles')
f1.fit()
print(f1)








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




