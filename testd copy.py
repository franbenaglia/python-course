from scipy.integrate import quad
from numpy import log, sin

def integrand(x):
    return log(sin(x))

print(quad(integrand, 0, 2))