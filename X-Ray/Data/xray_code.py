import spinmob as s
from numpy import pi, exp, real
from scipy.special import wofz, erf
ROOT2 = 2.0**0.5 # Code speedup

#peak1 = s.data.load('Cu-100-09-01.UXD')
#peak2 = s.data.load('Cu-75-Ni-25-09-01.UXD')
#peak3 = s.data.load('Cu-50-Ni-50-09-01.UXD')
#peak4 = s.data.load('Cu-25-Ni-75-10-01.UXD')
#peak5 = s.data.load('Ni-100-09-01.UXD')
#alloy_legend = ["Cu100", "Cu75", "Cu50", "Cu25", "Cu0"]
#
#s.plot.xy.data([peak1[0],peak2[0],peak3[0],peak4[0],peak5[0]],\
#                [peak1[1],peak2[1],peak3[1],peak4[1],peak5[1]],\
#                yshift = 150,\
#                xlabel = 'Angle 2theta',\
#                ylabel = 'Intensity [Counts]',\
#                label = alloy_legend,\
#                legend = 'right')


### FITTING
# Voigt function
def voigt(x, sigma=1, gamma=1):
    """
    Returns a Voigt function (a convolution of a Lorentzian and Gaussian) 
    centered at x=0 with Gaussian standard deviation sigma and Lorentzian 
    half-width gamma. The function is normalized to have unity area.
    
    Parameters
    ----------
    x:
        Distance from center of peak.
    sigma = 1:
        Standard deviation of Gaussian ~ exp(-x**2/(2*sigma**2)) 
    gamma = 1:
        Halfwidth of Lorentzian ~ 1/(1+x**2/gamma**2)
    """
    return real(wofz((x + 1j*gamma)/sigma/ROOT2)) / sigma / (2*pi)**0.5            
            
# Create a fitter object
f = s.data.fitter()

# Define the fit functions (in this case, the sum of two Lorentzians) and floating parameters.
f.set_functions('A*V(x-x0,s,a)', 'A, x0, s, a', V=voigt)

# Load a *.txt data file
d = s.data.load(filters="*.UXD")

# Stick the data into the fitter object
y_error = d[1]**(1/2)
f.set_data(xdata=d[0], ydata=d[1], eydata=y_error)

# Set some of the guess parameters
#f.set(s = 0.1, a = 0.2)

# Fun trick: have the user click to make guess parameters!
print("CLICK THE PEAKS!!")
click_x1, click_y1 = f.ginput()[0]
#click_x2, click_y2 = f.ginput()[0]

# make a better guess for a and x0, trim the data, and label the axes!
f.set(A=click_y1, x0=click_x1,
      xlabel='Pants (mV)',
      ylabel='Shoes (nm)')

# Fit!
f.fit()

# show the results (see spinmob wiki for more details!)
print(f)





