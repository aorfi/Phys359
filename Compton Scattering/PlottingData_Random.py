#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 15:06:33 2019

@author: Elisa
"""
import spinmob as s
import numpy as np
import matplotlib.pyplot as plt


rod = s.data.load('ENal_20deg.dat')
norod = s.data.load('ENnorod_20deg.dat')

x = rod[0]
y1 = rod[1]
y2 = norod[1]
alloy_legend = ["Rod", "NoRod"]
s.plot.xy.data([x,x],\
                  [y1,y2],\
                  xlabel = 'Energy',\
                  ylabel = 'Counts',\
                  title = '27deg',\
                  label = alloy_legend,\
                  legend = 'right')

