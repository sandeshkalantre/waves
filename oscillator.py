import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#number of simulation points
N = 100
t = np.linspace(0,500,N)

#damping
gamma = 0.01
#natural frequency
w_0 = 5

def dy_dt(y,t):
    return np.array([y[1],gamma*y[1] - w_0**2 * y[0]])

#initial conditions
y0 = np.array([2,0])

result = odeint(dy_dt,y0,t)

plt.plot(t,result[:,0],label=r'$\gamma = $' + str(gamma) + ' $\omega_0 = $' + str(w_0) + '$\\ x_0 = $' + str(y0[0]) + ' $v_0 = $' + str(y0[1]),linewidth=3.0)
plt.plot([0,10],[0,0],'r--',linewidth=3.0)
plt.xlabel('Time',fontsize=24)
plt.ylabel('x',fontsize=24)
plt.legend(fontsize=14)
plt.ylim([-2,2])
plt.show()

