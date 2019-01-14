"""
This file shows you how to load an image into a numpy array.

You may need to intsall imageio, which can be done with

   conda install imageio

from the system terminal (or anaconda navigator)
"""
import spinmob
import imageio

# As the user for an image
path = spinmob.dialogs.open_single()

# Load the image into array "a". 
a = imageio.imread(path)

"""
"a" will be a 3D array: Two indices for the pixel position (x and y), 
and one index for the color, which can have either 3 values (RGB) or 4 (RGBA).
"""

# Plot the green channel
spinmob.plot.image.data(a[:,:,2])

"""
You can also do fun stuff like summing all of the rows or columns.
Try, e.g. a[:,:,2].sum(axis=1) to get a 1D array of summed columns.
"""
