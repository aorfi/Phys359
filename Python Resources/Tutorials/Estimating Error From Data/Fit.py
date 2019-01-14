import spinmob


# Create a fitter object
f = spinmob.data.fitter()

# Define the fit function (in this case, a constant) and fit parameters.
f.set_functions(f='a', p='a')

# Load a *.txt data file
d = spinmob.data.load(filters="*.txt")

# Stick the data into the fitter object, and make an initial guess at the error bar
f.set_data(xdata=d[0], ydata=d[1], eydata=1)

# Fit!
f.fit()

# Show the results (see spinmob wiki for more details!)
print(f)