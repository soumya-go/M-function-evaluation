# M-function Evaluation

This repository evaluates the values of the M(μ, U, ω) function across its entire parameter space.

The **zero albedo** case allows an analytical solution. For the **general case**, `M_func.py` uses Gauss–Legendre quadrature to compute the triple-valued function numerically.

---

## Example Plot

Below is the behavior of the M-function for the zero albedo case:

![M vs μ (Zero Albedo)](M_vs_mu_zeroalbdo.jpg)

---

## Files

All the files must be located in the **same folder** for the code to work properly:

- **`M_func.py`**: Core function evaluator using Gauss–Legendre quadrature.
- **`M_parameter_test.py`**: Test script to interact with `M_func.py`.
- **`M_func_albdo_0.py`**: Simplified script for the zero albedo (ω = 0) analytical case.
- **`M_vs_mu_zeroalbdo.jpg`**: Example plot for the zero albedo case (μ vs M-function).
- **`example_table.tex`**: LaTeX code containing the example table for the analytical solution.

A simple script for the analytical (zero albedo) case is provided in `M_func_albdo_0.py`.  
An example plot is shown above (`M_vs_mu_zeroalbdo.jpg`), and the corresponding table is included in `example_table.tex`.

---

## Dependencies

This project requires:

- [Python 3](https://www.python.org/)
- [NumPy](https://numpy.org/)
- [SciPy](https://scipy.org/)

Install the dependencies using pip:

```bash
pip install numpy scipy
