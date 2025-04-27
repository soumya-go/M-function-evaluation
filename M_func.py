import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.interpolate import interp1d
import sys as s

def solve_M_gauss_legendre(U, omega_tilde_0, num_points=100, tol=1e-8, max_iter=1000):
    """
    This function calculates the values of M(mu,U,omega_tilde_0) for a range of mu values.
    It returns the mu_values, M_values and the interpolator function
    """
    # Gauss-Legendre quadrature nodes and weights on [0, 1]
    nodes, weights = leggauss(num_points)
    mu_vals = 0.5 * (nodes + 1)  # transform from [-1,1] to [0,1]
    weights = 0.5 * weights

    # Initialize M(mu) = 1
    M = np.ones_like(mu_vals)

    for iteration in range(max_iter):
        M_old = M.copy()

        # Interpolation-like update (vectorized)
        for i, mu in enumerate(mu_vals):
            # Compute integral ∫ M(μ') / (μ + μ') dμ' using Gauss-Legendre quadrature
            integrand = M_old / (mu + mu_vals)
            integral = np.sum(weights * integrand)

            # Update M(mu)
            term1 = 1
            term2 = 2 * U * M_old[i] * mu * np.log(1 + 1 / mu)
            term3 = mu * M_old[i] * (omega_tilde_0 / 2) * integral

            M[i] = term1 + term2 + term3

        # Convergence check
        if np.linalg.norm(M - M_old, ord=np.inf) < tol:
            print(f"Converged in {iteration} iterations.")
            interpolator = interp1d(mu_vals, M, kind='cubic', fill_value="extrapolate")
            break
    else:
        print("Did not converge within max iterations.")
        s.exit(1)

    return mu_vals, M,interpolator
    
if __name__=="__main__":
    
    #Output loop
    #U_T=[0.0,0.1,0.2,0.3,0.4,0.5,0.6]
    U_T=[0.0,0.1,0.2,0.3,0.4,0.5] # for omg = 0.1
    #U_T=[0.0,0.1,0.2,0.3,0.4,0.45] # for omg = 0.2
    #U_T=[0.0,0.1,0.2,0.25,0.3,0.35]	# for omg = 0.3
    #U_T=[0.0,0.1,0.15,0.2,0.25,0.3]	# for omg = 0.4
    #U_T=[0.0,0.05,0.1,0.15,0.2,0.25]	# for omg = 0.5
    #U_T=[0.0,0.05,0.1,0.15,0.175,0.2]	# for omg = 0.6
    #U_T=[0.  , 0.02, 0.04, 0.06, 0.08, 0.1 ]	# for omg = 0.7
    #U_T=[0.  , 0.02, 0.04, 0.06, 0.08, 0.09 ]	# for omg = 0.8
    #U_T=[0.  ,0.01, 0.02, 0.03,0.04 ]	# for omg = 0.9
    #U_T=[0.  ,0.01, 0.02 ]	# for omg = 0.95
    #U_T= [0.1,0.2,0.3]
    U_T=[0.0]

    M_final = []
    for U in U_T:
        omega_tilde_0 = 0.1

        a,M,M_interpolator = solve_M_gauss_legendre(U, omega_tilde_0, num_points=100, tol=1e-6, max_iter=1000)
        print(len(M))

        # User-defined mu values
        user_mu = np.linspace(0.,1.0,21)#np.array([0.05, 0.2, 0.5, 0.85, 0.99])  # Example user-defined mu values
        user_M = M_interpolator(user_mu)  # Compute interpolated H(mu)

        print(" User μ      M(μ)")
        print("---------------------")
        for mu, M in zip(user_mu, user_M):
            print(f"{M:.6f}")
        M_final.append(user_M)
        print("Done for U=",U)
    """		
    with open("M(omg_"+str(omega_tilde_0)+")_output.txt", "w") as file:
        file.write("# M-function values \n")#("# M-function values (omega_tilde ="+str(omega_tilde_0)+", U(T) = "+str(U)")\n")
            
        file.write("#--------------------------------------------------\n")
        file.write("#   mu        U="+str(U_T[0])+"			U="+str(U_T[1])+"			U="+str(U_T[2])+"			U="+str(U_T[3])+"			U="+str(U_T[4])+"			U="+str(U_T[5])+"			U="+str(U_T[6])+"\n")
        file.write("#--------------------------------------------------\n")
        for mu, M0,M1,M2,M3,M4,M5,M6 in zip(user_mu, M_final[0],M_final[1],M_final[2],M_final[3],M_final[4],M_final[5],M_final[6]):
            file.write(f"{mu:.3f}    {M0:.4f}    {M1:.4f}    {M2:.4f}    {M3:.4f}    {M4:.4f}    {M5:.4f}    {M6:.4f}\n")
    #"""
