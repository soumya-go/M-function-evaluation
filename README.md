# M-function Evaluation

This code evaluates the values of the M(μ, U, ω)-function in all of its parameter space.  
The zero albedo case is the only possible analytical solution, whereas the `M_func.py` script is the most general version to calculate the triple-valued function using the Gauss–Legendre formula. The dependencies are Python with SciPy and NumPy installed in the system.

The `M_parameter_test.py` script provides a handle to the original `M_func.py` evaluation code.

A simplistic script for the analytical case is given in the script `M_func_albdo_0.py`.  
An example plot can be found below for the zero albedo case:

![M vs μ (Zero Albedo)](M_vs_mu_zeroalbdo.jpg)

We have also added the example table:

## Example Table (Zero Albedo Case)

An example table showing the evaluated M-function values for various values of **μ** and **U** at zero albedo:

| μ     | U=0.1   | U=0.2   | U=0.3   | U=0.4   | U=0.5   | U=0.6   | U=0.7    |
|-------|---------|---------|---------|---------|---------|---------|----------|
| 0     | 1       | 1       | 1       | 1       | 1       | 1       | 1        |
| 0.05  | 1.0314  | 1.06484 | 1.10052 | 1.13867 | 1.17956 | 1.2235  | 1.27084  |
| 0.1   | 1.05037 | 1.10609 | 1.16805 | 1.23737 | 1.31543 | 1.404   | 1.50536  |
| 0.15  | 1.06508 | 1.13923 | 1.22447 | 1.3235  | 1.43995 | 1.57888 | 1.74747  |
| 0.2   | 1.0772  | 1.16733 | 1.2739  | 1.4019  | 1.55849 | 1.75445 | 2.00679  |
| 0.25  | 1.08751 | 1.19182 | 1.31825 | 1.47468 | 1.67325 | 1.93361 | 2.28992  |
| 0.3   | 1.09647 | 1.21353 | 1.35859 | 1.54302 | 1.7854  | 2.11811 | 2.60323  |
| 0.35  | 1.10436 | 1.23303 | 1.39564 | 1.60766 | 1.89564 | 2.3093  | 2.9539   |
| 0.4   | 1.11138 | 1.25069 | 1.42993 | 1.66913 | 2.00443 | 2.50832 | 3.35061  |
| 0.45  | 1.1177  | 1.26681 | 1.46182 | 1.72779 | 2.11208 | 2.7162  | 3.80438  |
| 0.5   | 1.12342 | 1.2816  | 1.49161 | 1.78395 | 2.2188  | 2.93399 | 4.32954  |
| 0.55  | 1.12863 | 1.29524 | 1.51955 | 1.83783 | 2.32477 | 3.16276 | 4.94537  |
| 0.6   | 1.1334  | 1.30787 | 1.54583 | 1.88964 | 2.43012 | 3.40364 | 5.67848  |
| 0.65  | 1.13779 | 1.31962 | 1.57062 | 1.93953 | 2.53494 | 3.65785 | 6.56676  |
| 0.7   | 1.14184 | 1.33057 | 1.59405 | 1.98764 | 2.6393  | 3.92672 | 7.66619  |
| 0.75  | 1.1456  | 1.34082 | 1.61625 | 2.03409 | 2.74328 | 4.21173 | 9.06312  |
| 0.8   | 1.14909 | 1.35043 | 1.63732 | 2.07898 | 2.84693 | 4.51453 | 10.8982  |
| 0.85  | 1.15235 | 1.35947 | 1.65736 | 2.12242 | 2.95028 | 4.83696 | 13.4171  |
| 0.9   | 1.1554  | 1.36798 | 1.67643 | 2.16448 | 3.05337 | 5.18112 | 17.0911  |
| 0.95  | 1.15826 | 1.37602 | 1.69463 | 2.20523 | 3.15623 | 5.54938 | 22.9532  |
| 1     | 1.16094 | 1.38362 | 1.712   | 2.24476 | 3.25889 | 5.94448 | 33.7907  |

## Usage

