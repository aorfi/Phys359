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



#get dot positions
imgdots = io.imread("test.jpg")[2050:2150,1700:2800]
imgdots = io.imread("test.jpg")[700:1500][50:5500]
imdots = rgb2gray(imgdots)
imdotsT = np.ndarray.transpose(imdots)
avDot = np.empty(imdots[0].size)

for i in range(imdots[0].size):
    avDot[i] = np.average(imdotsT[i])
    
max1 = np.amax(avDot[0:600])



xdots = np.arange(0,imdots[0].size,1)
peakx = xdots[1900:2200]
peaky = avDot[1900:2200]
ytotal = np.sum(avDot[1900:2200])
xtotal = peakx.size
avarray = np.empty(peakx.size)
for i in range(peakx.size):
    avarray[i] = (peaky[i]/ytotal)*xdots[1900+i]
average = np.sum(avarray)
xaverage = np.empty(peakx.size)
xaverage.fill(average)



fig, axs = plt.subplots(2, 2)

axs[0,0].imshow(imdots, cmap=plt.cm.gray)


axs[1,0].plot(xdots,avDot, 'r')


axs[0,1].plot(peakx,peaky, 'r')




plt.show()



    

#Average distance





#peak fitting of the graph paper

#def voigt(x, sigma, gamma):
#    return real(wofz((x + 1j*gamma)/sigma/ROOT2)) / sigma / (2*pi)**0.5 
#
#def guassian(x,x1,w):
#    return np.exp(-((x-x1)**2)/(2*w**2))
#
#f1 = spinmob.data.fitter()
##f1.set_functions('A1*V(x-x1,s1,a1)+A2*V(x-x2,s2,a2)+c', 
##                'A1, x1, s1, a1,A2, x2, s2, a2, c=0', V= voigt)
#f1.set_functions('A1*G(x,x1,w)+c', 
#               'A1, x1, w,  c=0', G= guassian)
#peakx = x[465:510]
#peaky = onLine[465:510]
#f1.set_data(peakx, peaky, 0.001)
#f1.set(w=4)
#click_x1, click_y1 = f1.ginput()[0]
##click_x2, click_y2 = f1.ginput()[0]
#f1.set(A1=click_y1, x1=click_x1, plot_guess = True, 
#      xlabel='Relative Brightness',
#      ylabel='Pixles')
#f1.fit()
#print(f1)

#peak fitting of diffraction pattern
#def guassian(x,x1,w):
#    return np.exp(-((x-x1)**2)/(2*w**2))
#f1 = spinmob.data.fitter()
#f1.set_functions('A1*G(x,x1,w)+c', 
#               'A1, x1, w,  c=0', G= guassian)
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




