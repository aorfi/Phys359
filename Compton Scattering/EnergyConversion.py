# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 17:32:02 2019

@author: aorfi
"""
import spinmob as s
import numpy as np

data = s.data.load('4brick.dat')
EnData =np.zeros((data[0].size,data[1].size))

#converts data to energy 
for i in range(data[0].size):
    EnData[1][i] = data[1][i]
    EnData[0][i] = (data[0][i]-0.056)/(0.556622)
    
#s.plot.xy.data(data[0], EnData[1])
    
#saves files
d = s.data.databox()
d[0]=EnData[0]
d[1]=EnData[1]
#d.save_file()

d1 = s.data.databox()
d1[0] = d[0]
d1[i] = np.zeros(d1[0].size)
for i in range(d1[0].size):
     a = d[0][i]
     eff = 1/100*(2.5*10**(-12)*a**5 - 6.3*10**(-9)*a**4 + 5.9*10**(-6)*a**3 - 0.0023*a**2 + 0.17*a + 95) #efficiancy curve
     d1[1][i] = d[1][i]/eff
d1.save_file()


