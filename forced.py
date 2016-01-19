import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#number of simulation points
N = 1000

#damping
gamma = 1
#natural frequency
w_0 = 5
#Forced oscillator amplitude
F_0 = 4
#Forced oscillator frequency
w = 10
eps = 1e-15

T_max = 15*2*np.pi/w_0
t = np.linspace(0,T_max,N)
def F(t):
    return F_0 * np.cos(w * t) 
def dy_dt(y,t):
    return np.array([y[1]+eps,eps-1.0 * gamma*y[1] - w_0**2 * y[0] + F(t)])

#initial conditions
y0 = np.array([2,0])

result = odeint(dy_dt,y0,t)
plt.plot(t,result[:,0],label=r'$\gamma = $' + str(gamma) + ' $\omega_0 = $' + str(w_0) + '$\\ x_0 = $' + str(y0[0]) + ' $v_0 = $' + str(y0[1]),linewidth=2.0)
plt.plot(t,F(t),label=r'$F(t) = $' + str(F_0) + '$\cos($' + str(w) + '$t)$',linewidth=2.0)
plt.plot([0,T_max],[0,0],'r--',linewidth=3.0)
plt.xlabel(r'Time$(t)$',fontsize=16)
plt.ylabel(r'$x$',fontsize=16)
plt.legend(fontsize=14)
plt.ylim([-5,5])
plt.show()

