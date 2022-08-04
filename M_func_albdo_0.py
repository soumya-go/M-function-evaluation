# This code eavaluates the values of M(mu)- function in case of zero scattering albedo.
# It evaluates the values of M-function for different values of the parameter U.

import numpy as np, sys as s
import matplotlib.pyplot as plt



mu = np.arange(0.05,1.05,0.05)  # Here mu is defined to vary from 0.05 to 1. We do not include mu=0 as it gives zero division error in calculation. 
U=np.arange(0.1,0.8,0.1) # The values of U vary from 0.1 to 0.7. Because for U>0.72 M-function becomes negative which is unphysical.     

# Here we define the M -function which is defined by the following formula except mu=0
def M_func(mu,U):
        z = 1./(1-2*U*mu*np.log(1+1./mu))
        return np.array([1]+list(z)) # Here the element 1 is the value for mu=0

M = [] #defining the list carries M-function values.

for i in range(len(U)):
        M.append(M_func(mu,U[i]))


mu = np.array([0]+list(mu))
H = np.ones(len(mu))# Chandrasekhar's H-function for no scattering albedo.
# CAUTION: mu=0 is included in the mu array. The calling of m-function is not permitted afterwards.

#"""
#================================================
#===================Plotting=====================
#================================================
plt.plot(mu,H,"k--")
for j in range(len(U)-1):
        plt.plot(mu,M[j])
#plt.legend(["U="+str(k) for k in U])
plt.legend(["$H(\mu)$","U=0.1","U=0.2","U=0.3","U=0.4","U=0.5","U=0.6"])
plt.xlabel("$\mu$");plt.ylabel("$M(\mu)$")
#plt.savefig("M_vs_mu_zeroalbdo.jpg") # Uncomment this line only if you want to save the plotted figure.
plt.show()
#"""
#================================================
#============Tabulation of the values============
#================================================
from tabulate import tabulate
table = []
for l in range(len(mu)):
        a = [mu[l],M[0][l],M[1][l],M[2][l],M[3][l],M[4][l],M[5][l],M[6][l]]
        table.append(a)
print tabulate(table,headers=["mu","U=0.1","U=0.2","U=0.3","U=0.4","U=0.5","U=0.6","U=0.7"])
print "working"
