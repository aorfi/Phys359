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
def voigt(x, sigma, gamma):
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

# Define the fit functions (in this case, the sum of two Lorentzians) 
# and floating parameters.
f.set_functions('A1*V(x-x1,s1,a1)+ A2*V(x-x2,s2,a2) + A3*V(x-x3,s3,a3) + A4*V(x-x4,s4,a4) + A5*V(x-x5,s5,a5)',\
                'A1, x1, s1, a1, A2, x2, s2, a2, A3, x3, s3, a3, A4, x4, s4, a4, A5, x5, s5, a5', V=voigt)

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
click_x2, click_y2 = f.ginput()[0]
click_x3, click_y3 = f.ginput()[0]
click_x4, click_y4 = f.ginput()[0]
click_x5, click_y5 = f.ginput()[0]


# make a better guess for a and x0, trim the data, and label the axes!
f.set(A1=click_y1, x1=click_x1,
      A2=click_y2, x2=click_x2,
      A3=click_y3, x3=click_x3,
      A4=click_y4, x4=click_x4,
      A5=click_y5, x5=click_x5,
      xlabel='Pants (mV)',
      ylabel='Shoes (nm)')

# Fit!
f.fit()

# show the results (see spinmob wiki for more details!)
print(f)





