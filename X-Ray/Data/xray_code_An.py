#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:20:37 2019

@author: vuongthaian
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 14:16:01 2019

@author: vuongthaian
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import spinmob as s
peak1 = s.data.load('Cu-100-09-01.UXD')
peak2 = s.data.load('Cu-75-Ni-25-09-01.UXD')
peak3 = s.data.load('Cu-50-Ni-50-09-01.UXD')
peak4 = s.data.load('Cu-25-Ni-75-10-01.UXD')
peak5 = s.data.load('Ni-100-09-01.UXD')
alloy_legend = ["Cu100", "Cu75", "Cu50", "Cu25", "Cu0"]

s.plot.xy.data([peak1[0],peak2[0],peak3[0],peak4[0],peak5[0]],\
                [peak1[1],peak2[1],peak3[1],peak4[1],peak5[1]],\
                yshift = 150,\
                xlabel = 'Angle 2theta',\
                ylabel = 'Intensity [Counts]',\
                label = alloy_legend,\
                legend = 'right')

s.plot.xy.data([peak1[0],peak2[0],peak3[0],peak4[0],peak5[0]],\
                [peak1[1],peak2[1],peak3[1],peak4[1],peak5[1]])




