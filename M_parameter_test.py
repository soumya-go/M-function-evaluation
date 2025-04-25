# Use of M_func for different user defined values.
# Here the function is treated as three parameter function mu, U and omega.

import numpy as np
import matplotlib.pyplot as plt
from M_func import solve_M_gauss_legendre

def M(mu=0.,U=0.,omega=0.1):
    mu_val,M_val,interpolator= solve_M_gauss_legendre(U,omega)
    return interpolator(mu)

mu= np.array([0.1,0.5,1.0])

#omega = np.linspace(0.1,0.5,20)
U_val=np.linspace(0.1,0.4,20)
for j in range(len(mu)):
    M_values=[]
    for i in range(len(U_val)):
        M_values.append(M(mu[j],U=U_val[i],omega=0.2))
    plt.plot(U_val,M_values)
plt.xlabel("U");plt.ylabel("M")
plt.show()

