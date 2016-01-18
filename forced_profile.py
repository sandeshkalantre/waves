
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#number of simulation points
N = 100

#damping
gamma = 1
#natural frequency
w_0 = 5
#Forced oscillator amplitude
F_0 = 4

eps = 1e-8

#forced oscillator
def F(t,w):
    return F_0 * np.cos(w * t) 

def dy_dt(y,t,w):
    return np.array([y[1]+eps,eps-1.0 * gamma*y[1] - w_0**2 * y[0] + F(t,w)])


def dummy_A(w):
    T_max = 15*2*np.pi/w_0
    t = np.linspace(0,T_max,N)
    #initial conditions
    y0 = np.array([2,0])
    
    result = odeint(dy_dt,y0,t,args=(w,))
    amplitude = np.amax(result[N-0.5*N:N,0])
    return amplitude
A = np.vectorize(dummy_A)
w_max = 10*w_0
w_array = np.linspace(0,w_max,N)
plt.plot(w_array,A(w_array),label=r'$A(\omega)$')
plt.plot([[w_0,w_0],[0,4]],'r--')
plt.ylabel(r'$A(\omega)$',fontsize=16)
plt.xlabel(r'$\omega$',fontsize=16)
plt.legend(fontsize=24)
plt.show()
