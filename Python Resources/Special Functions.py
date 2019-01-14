from numpy import pi, exp, real
from scipy.special import wofz, erf
ROOT2 = 2.0**0.5 # Code speedup

def erfcx(x):
    """
    Scaled complementary error function.
    """
    return exp(x**2)*(1-erf(x))

def em_gaussian(x, sigma=1, tau=1):
    """
    Returns an exponentially modified Gaussian (a convolution of an exponential
    cutoff at x=0 and Gaussian) having standard deviation sigma and exponential 
    decay length tau. This function is normalized to have unity area.
    
    Parameters
    ----------
    x:
        Distance from the center of the peak.
    sigma:
        Standard deviation of Gaussian ~ exp(-x**2/(2*sigma**2))
    tau:
        Length scale of exponential ~ exp(x/tau). Positive tau skews the peak 
        to higher values and negative tau skews to lower values.
    """
    t = abs(tau)
    s = sigma
    
    if tau >= 0: return 0.5/t*exp(-0.5*( x/s)**2)*erfcx((s/t - x/s)*0.5**0.5)
    else:        return 0.5/t*exp(-0.5*(-x/s)**2)*erfcx((s/t + x/s)*0.5**0.5)

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



# Example Fitter: see https://github.com/Spinmob/spinmob/wiki/4.-Fitting#advanced-function-fitting
# f = spinmob.data.fitter()
# f.set_functions('A*V(x-x0,s,a)', 'A, x0=3, s=0.2, a=0.2', V=voigt)