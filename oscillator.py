import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#number of simulation points
N = 100
t = np.linspace(0,50,N)

#damping
gamma = 0.1
#natural frequency
w_0 = 1

def dy_dt(y,t):
    return np.array([y[1],-1.0 * gamma*y[1] - w_0**2 * y[0]])

#initial conditions
y0 = np.array([2,0])


result = odeint(dy_dt,y0,t)

plt.plot(t,result[:,0],label=r'$\gamma = $' + str(gamma) + ' $\omega_0 = $' + str(w_0))
plt.xlabel('Time')
plt.ylabel('x')
plt.legend()
plt.grid(True)
plt.show()

