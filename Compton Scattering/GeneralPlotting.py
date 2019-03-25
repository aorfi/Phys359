# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 14:55:52 2019

@author: aorfi
"""

import spinmob as s

#peak1 = s.data.load('cuAu-sampleA-14-01.UXD')

positive = s.data.load('zeroangle_15deg.dat')
negative = s.data.load('zeroangle_-15deg.dat')

alloy_legend = ["Sample A", "Sample B"]

s.plot.xy.data([positive[0],negative[0]],\
                [positive[1],negative[1]],\
                xlabel = 'Bin',\
                ylabel = 'Counts',\
                label = alloy_legend,\
                legend = 'right')
#s.plot.xy.data(peak1[0], peak1[1])
#s.plot.xy.data(peak2[0], peak2[1]