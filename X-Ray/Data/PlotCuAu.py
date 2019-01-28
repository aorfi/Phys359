#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 17:41:10 2019

@author: Elisa
"""


import spinmob as s

#peak1 = s.data.load('cuAu-sampleA-14-01.UXD')

peak1 = s.data.load('cuAu-sampleA-14-01.UXD')
peak2 = s.data.load('cu3Au-sampleB-14-01.UXD')
peak3 = s.data.load('Cu-100-09-01.UXD')
#peak5 = s.data.load('Sn-100-10-01.UXD')
alloy_legend = ["Sample A", "Sample B", "100% Copper"]
initial = 10
final1 = 110
#final2 = 46
##final3 = 48
##final4 = 54
#increment = 0.05
f1 = int((final1 - initial)/0.05)
f2 = int((final1 - initial)/0.05)
f3 = int((final1 - initial)/0.05)
#f4 = int((final4 - initial)/0.05)

s.plot.xy.data([peak1[0],peak2[0],peak3[0]],\
                [peak1[1],peak2[1],peak3[1]],\
                yshift = 150,\
                xlabel = '2'r'$\theta$',\
                ylabel = 'Intensity [Counts]',\
                label = alloy_legend,\
                legend = 'right')
#s.plot.xy.data(peak1[0], peak1[1])
#s.plot.xy.data(peak2[0], peak2[1])