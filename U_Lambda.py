# Calculation of U as a function of lambda for the observational range
import numpy as np
import matplotlib.pyplot as plt, sys as s

# Constants (SI units)
h = 6.62607015e-34  # Planck constant (J·s)
c = 2.99792458e8    # Speed of light (m/s)
k = 1.380649e-23    # Boltzmann constant (J/K)
R_sun = 6.957*1e8   # Solar radius (m)
AU = 1.496*1e11     # Astronomical unit (m)

def planck(wavelength, T):
    """Planck's law: spectral radiance as a function of wavelength and temperature"""
    a = 2.0 * h * c**2
    b = h * c / (wavelength * k * T)
    return a / (wavelength**5 * (np.exp(b) - 1.0))

# System properties
name = "K2-137b"
Tp = 1471 #Planetary temperature (in K)
Ts = 3492 # Star Temperature (in K)
D = 0.0058*AU # Star-Planet distance (m)
R_star = 0.442*R_sun #Radius of the star (in m)

# Wavelength range (in meters)
wavelength = np.linspace(1e-7, 3e-5, 1000)  # 100 nm to 30000 nm

# Compute the U 
Bp = planck(wavelength, Tp)
Bs = planck(wavelength, Ts)

U= (Bp/Bs)*(D/R_star)**2


#Plotting
plt.figure(figsize=(8, 7))
#plt.plot(wavelength * 1e9, B1)
#plt.plot(wavelength * 1e9, B2)
plt.plot(wavelength * 1e9, U,"k-")  # convert to nm for plotting
plt.ylim(0,0.7);plt.xlim(0,3000)
plt.xlabel("Wavelength (nm)",fontsize=14)
plt.ylabel(f"$U_\lambda$",fontsize=14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title(name,fontsize=16)
#plt.grid(True)
plt.tight_layout()
plt.savefig("./Plots/Uvsl_K2137b.jpg",dpi=200)
plt.show()
#
