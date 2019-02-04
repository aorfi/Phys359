import spinmob as s
from numpy import pi, exp, real
from scipy.special import wofz, erf
ROOT2 = 2.0**0.5 # Code speedup


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
## Initiate file names and stuffs 
files = ['Cu-100-09-01.UXD', 'Cu-75-Ni-25-09-01.UXD', 'Cu-50-Ni-50-09-01.UXD',
         'Cu-25-Ni-75-10-01.UXD', 'Ni-100-09-01.UXD'] 
theta2 = []
theta2_err = []

         
for num in range (1,6): 
    # Create a fitter object
    f1 = s.data.fitter()
    f2 = s.data.fitter()
    f3 = s.data.fitter()
    f4 = s.data.fitter()
    #f5 = s.data.fitter()
    
    # Define the fit functions (in this case, the sum of two Lorentzians) 
    # and floating parameters.
    #f.set_functions('A1*V(x-x1,s1,a1)+ A2*V(x-x2,s2,a2) + A3*V(x-x3,s3,a3) + A4*V(x-x4,s4,a4) + A5*V(x-x5,s5,a5)',\
    #                'A1, x1, s1, a1, A2, x2, s2, a2, A3, x3, s3, a3, A4, x4, s4, a4, A5, x5, s5, a5', V=voigt)
    f1.set_functions('A1*V(x-x1,s1,a1)', 'A1, x1, s1, a1', V= voigt)
    f2.set_functions('A2*V(x-x2,s2,a2)', 'A2, x2, s2, a2', V= voigt)
    f3.set_functions('A3*V(x-x3,s3,a3)', 'A3, x3, s3, a3', V= voigt)
    f4.set_functions('A4*V(x-x4,s4,a4)', 'A4, x4, s4, a4', V= voigt)
    #f5.set_functions('A5*V(x-x5,s5,a5)', 'A5, x5, s5, a5', V= voigt)
    
    # Load a *.txt data file
    d = s.data.load(files[num-1])
    
    # Stick the data into the fitter object
    y_error = d[1]**(1/2)
    f1.set_data(xdata=d[0], ydata=d[1], eydata=y_error)
    f2.set_data(xdata=d[0], ydata=d[1], eydata=y_error)            
    f3.set_data(xdata=d[0], ydata=d[1], eydata=y_error)            
    f4.set_data(xdata=d[0], ydata=d[1], eydata=y_error)            
    #f5.set_data(xdata=d[0], ydata=d[1], eydata=y_error, plot_guess = 'False')        
    
    # Set some of the guess parameters
    #f.set(s1 = 0.2, a1 = 0.2, s2= 0.2, a2 = 0.2, s3= 0.2, a3 = 0.2,s4= 0.2, a4 = 0.2,\
    #      s5 = 0.2, a5 = 0.2, ymin = 10)
    f1.set(s1 = 0.2, a1 = 0.2, ymin = 13)
    f2.set(s2 = 0.2, a2 = 0.2, ymin = 13)
    f3.set(s3 = 0.2, a3 = 0.2, ymin = 13)
    f4.set(s4 = 0.2, a4 = 0.2, ymin = 13)
    #f5.set(s5 = 0.2, a5 = 0.2, ymin = 15)
    
    # Fun trick: have the user click to make guess parameters!
    print("CLICK THE PEAKS!!")
    click_x1, click_y1 = f1.ginput()[0]
    click_x2, click_y2 = f2.ginput()[0]
    click_x3, click_y3 = f3.ginput()[0]
    click_x4, click_y4 = f4.ginput()[0]
    #click_x5, click_y5 = f5.ginput()[0]
    f1.set(xmin = click_x1 - 20, xmax = click_x1 + 20)
    f2.set(xmin = click_x2 - 20, xmax = click_x2 + 20)
    f3.set(xmin = click_x3 - 20, xmax = click_x3 + 20)
    f4.set(xmin = click_x4 - 20, xmax = click_x4 + 20)
    #f5.set(xmin = click_x5 - 20, xmax = click_x5 + 20)
    
    
    # make a better guess for a and x0, trim the data, and label the axes!
    f1.set(A1=click_y1, x1=click_x1, plot_guess = False, xlabel = '2'r'$\theta$',\
                    ylabel = 'Intensity [Counts]')
    f2.set(A2=click_y2, x2=click_x2, plot_guess = False, xlabel = '2'r'$\theta$',\
                    ylabel = 'Intensity [Counts]')
    f3.set(A3=click_y3, x3=click_x3, plot_guess = False, xlabel = '2'r'$\theta$',\
                    ylabel = 'Intensity [Counts]')
    f4.set(A4=click_y4, x4=click_x4, plot_guess = False, xlabel = '2'r'$\theta$',\
                    ylabel = 'Intensity [Counts]')
    #f5.set(A5=click_y5, x5=click_x5)
    
    
    # Fit!
    
    f2.fit()
    f3.fit()
    f4.fit()
    f1.fit()
    #f5.fit()
    
    
        
    
    # show the results (see spinmob wiki for more details!)
#    print(f1)
#    print(f2)
#    print(f3)
#    print(f4)
    #print(f5)
    
    ## Do data
    angle = []
    error = []
    mylist = [f1, f2, f3, f4]
    for i in range(1,5):
        a = mylist[i-1].results
        angle.append(a[0][1])
        error.append(np.sqrt(a[1][1][1]))
    
    theta2.append(angle)
    theta2_err.append(error)
    
    







