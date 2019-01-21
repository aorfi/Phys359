#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:27:58 2019

@author: vuongthaian
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:18:29 2019

@author: vuongthaian
"""

import spinmob as s

peak1 = s.data.load('Pb-100-10-01.UXD')
peak2 = s.data.load('Pb-75-Sn-25-14-01.UXD')
peak3 = s.data.load('Pb-50-Sn-50-14-01.UXD')
peak4 = s.data.load('Pb-25-Sn-75-14-01.UXD')
peak5 = s.data.load('Sn-100-10-01.UXD')
alloy_legend = ["Pb 100% - Sn 0%", "Pb 75% - Sn 25%", "Pb 50% - Sn 50%",
                "Pb 25% - Sn 75%", "Pb 0% - Sn 100%"]
initial = 10
final1 = 42
final2 = 46
final3 = 48
final4 = 54
increment = 0.05
f1 = int((final1 - initial)/0.05)
f2 = int((final2 - initial)/0.05)
f3 = int((final3 - initial)/0.05)
f4 = int((final4 - initial)/0.05)



s.plot.xy.data([peak1[0],peak2[0],peak3[0],peak4[0],peak5[0]],\
                [peak1[1],peak2[1],peak3[1],peak4[1],peak5[1]],\
                yshift = 150,\
                xlabel = '2'r'$\theta$',\
                ylabel = 'Intensity [Counts]',\
                label = alloy_legend,\
                legend = 'right')

#s.plot.xy.data([peak1[0][f1:f2],peak2[0][f1:f2],peak3[0][f1:f2],peak4[0][f1:f2],peak5[0][f1:f2]],\
#                [peak1[1][f1:f2],peak2[1][f1:f2],peak3[1][f1:f2],peak4[1][f1:f2],peak5[1][f1:f2]],\
#                yshift = 150,\
#                xlabel = '2'r'$\theta$',\
#                ylabel = 'Intensity [Counts]',\
#                label = alloy_legend,\
#                legend = 'left')
#
#s.plot.xy.data([peak1[0][f3:f4],peak2[0][f3:f4],peak3[0][f3:f4],peak4[0][f3:f4],peak5[0][f3:f4]],\
#                [peak1[1][f3:f4],peak2[1][f3:f4],peak3[1][f3:f4],peak4[1][f3:f4],peak5[1][f3:f4]],\
#                yshift = 150,\
#                xlabel = '2'r'$\theta$',\
#                ylabel = 'Intensity [Counts]',\
#                label = alloy_legend,\
#                legend = 'left')