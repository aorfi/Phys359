# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 14:58:35 2019

@author: aorfi
"""

from skimage import data, io, filters
import numpy as np
import matplotlib.pyplot as plt
image = skimage.data.load("test.jpg")

edges = filters.sobel(image)
io.imshow(edges)
io.show()