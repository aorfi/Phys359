# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 12:40:57 2019

@author: aorfi
"""
import spinmob as s
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks


d = s.data.load()
#s.plot.xy.data(d[0],d[1])

x=np.arange(1,10)
test= np.sin(x)




peaks,_ = find_peaks(d[1], height=100)
plt.plot(d[1])
len(peaks)
#plt.plot(peaks,test[peaks],"x")
plt.show()
print(peaks)



