# M-function Evaluation

This project provides code to evaluate the **M(μ, U, ω)** function across its full parameter space.

## Overview

- The **M-function** is evaluated using numerical methods due to the absence of an analytical solution—except in the **zero albedo case**, where an analytical form exists.
- The core logic is implemented in `M_func.py`, which calculates the triple-valued function using the **Gauss–Legendre quadrature** formula.
- The script `M_parameter_test.py` serves as a user-friendly interface to `M_func.py`, enabling easier testing and experimentation with parameters.
- A simplistic script for the analytical case is given in 

## Dependencies

- Python 3
- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)

You can install the dependencies using pip:

```bash
pip install numpy scipy
