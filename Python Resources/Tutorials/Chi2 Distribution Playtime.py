import scipy.stats as stats
import spinmob as sm

# Degrees of freedom
DOF = 2

# Plot the reduced chi^2 distribution
sm.plot.xy.function('DOF*P(x*DOF,DOF)', 1e-6, 5, 100000, 
                    g=dict(P=stats.chi2.pdf, DOF=DOF),
                    xlabel='$\chi^2_{red}$', 
                    ylabel='Probability Density Function')

# Running integral of probability distribution function
# This can be used to answer the question "how likely is it that I see
# this or larger value?"
sm.tweaks.integrate_shown_data()

# Move the figure to avoid confusing students
sm.tweaks.set_figure_window_geometry(position=[0,500])