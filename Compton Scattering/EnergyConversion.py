# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:32:02 2019

@author: aorfi
"""
import spinmob as s
import numpy as np

data = s.data.load('al_20deg.dat')
EnData =np.zeros((data[0].size,data[1].size))

for i in range(data[0].size):
    EnData[1][i] = data[1][i]
    EnData[0][i] = (data[0][i]-0.056)/(0.556622)
    
#s.plot.xy.data(data[0], EnData[1])
    
d = s.data.databox()
d[0]=EnData[0]
d[1]=EnData[1]
d.save_file()
    


