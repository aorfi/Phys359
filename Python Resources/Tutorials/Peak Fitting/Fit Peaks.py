import spinmob


# Create a fitter object
f = spinmob.data.fitter()

# Define the fit functions (in this case, the sum of two Lorentzians) and floating parameters.
f.set_functions('a1/(1+(x-x1)**2/w1**2) + a2/(1+(x-x2)**2/w2**2)', 
                'a1, x1, w1, a2, x2, w2')

# Load a *.txt data file
d = spinmob.data.load(filters="*.txt")

# Stick the data into the fitter object
f.set_data(xdata=d[0], ydata=d[1], eydata=d[2])

# Set some of the guess parameters
f.set(w1=20, w2=20)

# Fun trick: have the user click to make guess parameters!
print("CLICK THE PEAKS!!")
click_x1, click_y1 = f.ginput()[0]
click_x2, click_y2 = f.ginput()[0]

# make a better guess for a and x0, trim the data, and label the axes!
f.set(a1=click_y1, x1=click_x1, 
      a2=click_y2, x2=click_x2,
      xlabel='Pants (mV)',
      ylabel='Shoes (nm)')

# Fit!
f.fit()

# show the results (see spinmob wiki for more details!)
print(f)
