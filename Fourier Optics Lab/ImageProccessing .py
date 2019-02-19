# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:58:35 2019

@author: aorfi
"""
import numpy as np
import spinmob as s
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
xdots = np.arange(0,imdots[0].size,1)

for i in range(imdots[0].size):
    avDot[i] = np.average(imdotsT[i])

xmax = np.empty(9) 
ymax = np.empty(9) 
ymax[0] = np.amax(avDot[200:600])
xmax[0] = 200 + np.argmax(avDot[200:600])
ymax[1] = np.amax(avDot[600:1200])
xmax[1] = 600 + np.argmax(avDot[600:1200])
ymax[2] = np.amax(avDot[1300:1800])
xmax[2] = 1300 + np.argmax(avDot[1300:1800])
ymax[3] = np.amax(avDot[1800:2300])
xmax[3] = 1800 + np.argmax(avDot[1800:2300])
ymax[4] = np.amax(avDot[2300:3000])
xmax[4] = 2300 + np.argmax(avDot[2300:3000])
ymax[5] = np.amax(avDot[3000:3500])
xmax[5] = 3000 + np.argmax(avDot[3000:3500])
ymax[6] = np.amax(avDot[3500:4000])
xmax[6] = 3500 + np.argmax(avDot[3500:4000])
ymax[7] = np.amax(avDot[4000:4500])
xmax[7] = 4000 + np.argmax(avDot[4000:4500])
ymax[8] = np.amax(avDot[4500:5000])
xmax[8] = 4500 + np.argmax(avDot[4500:5000])


#Now, use these local max values to fit a line 
def line(m,b,x): 
    return m*x+b
#create fitter object : 
f = s.data.fitter()
f.set_functions('L(m,b,x)', 'm,b', L = line)
#set the data: 
y_err = np.empty(9) 
err = 7
for i in range (0,9): 
    y_err[i] = err

#define the array for peak number: 
peak_num = np.empty(9)
for i in range (0,9): 
    peak_num[i]=i
    
f.set_data(xdata=peak_num, ydata=xmax, eydata=y_err)
#set guess params: 
f.set(m=1, b=0)   
f.fit()
print(f)






fig, axs = plt.subplots(2, 2)

axs[0,0].imshow(imdots, cmap=plt.cm.gray)


axs[1,0].plot(xdots,avDot, 'r')
axs[1,0].axes.set_xlim([100,5000])
axs[1,0].plot(xmax,ymax, 'bo')



axs[0,1].plot(xdots,avDot, 'r')
axs[0,1].axes.set_xlim([100,5000])



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




