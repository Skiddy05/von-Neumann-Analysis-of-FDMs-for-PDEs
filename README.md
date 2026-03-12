# von Neumann Stability Analysis of Finite Difference PDE Solvers

**Course:** Mathematical Physics  
**Author:** Kshiteesh S (EP24BTECH11023)  
**Instructor:** Dr. Sangkha Borah

This independent project was taken up as a part of the course *EP2130 - Mathematical Physics* taught by Asst. Prof. Sangkha Borah.
---

## Overview: 

This project investigates the stability, dissipative, and dispersive properties of various Finite Difference Method (FDM) schemes through von Neumann Stability Analysis (vNSA). The analysis is applied to the solvers of two canonical PDEs:

- **The Linear Advection Equation** — $\frac{\partial f}{\partial t} + u \frac{\partial f}{\partial x} = 0$
- **The 1D Heat Equation** — $\frac{\partial f}{\partial t} = \alpha \frac{\partial^2 f}{\partial x^2}$

For each scheme, the amplification factor $G_k$ is derived analytically, and its magnitude and phase are used to characterise stability, dissipation, and dispersion. The theoretical predictions are then confirmed through numerical simulation.

---

## Project Summary:

### Linear Advection Equation 
| Scheme | Stability | Dissipation | Dispersion |
|---|---|---|---|
| FTCS (Forward Time – Centered Space) | Unconditionally Unstable | Anti-dissipative | Dispersive |
| BTCS (Backward Time – Centered Space) | Unconditionally Stable | Dissipative | Dispersive |
| Leapfrog | Stable if $\lambda \le 1$ | Non-dissipative | Dispersive |
| Lax–Friedrichs | Stable if $\lambda \le 1$ | Dissipative | Dispersive |
| Lax–Wendroff | Stable if $\lambda \le 1$ | Mildly dissipative | Dispersive |

### Heat Equation
| Scheme | Stability | Dissipation | Dispersion |
|---|---|---|---|
| FTCS | Stable if $r ≤ 0.5$ | Dissipative | Non-dispersive |
| BTCS (Backward Euler) | Unconditionally Stable | Strongly dissipative | Non-dispersive |
| Crank–Nicolson | Unconditionally Stable | Mildly dissipative | Non-dispersive |

$\lambda = u \frac{\Delta t}{\Delta x}$ (CFL number), $ r = \alpha \frac{\Delta t}{\Delta x^2} $ (diffusion number)

---

## Repository Structure

```
.
|-- FDM_Implementations.ipynb       # Main notebook: all FDM implementations and plots
|--Project report
|   |--vNSA_report.pdf  #
|   |-- Plots       # Folder containing all the relevant plots used in the Project Report
|   |-- Heatmap Plotters 
|-- requirements.txt                
|-- README.md                       
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- `pip` for package installation

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Skiddy05/von-Neumann-Analysis-of-FDMs-for-PDEs.git
   cd von-Neumann-Analysis-of-FDMs-for-PDEs
   ```

2. (Recommended) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux / macOS
   venv\Scripts\activate          # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Launch the notebook:
   ```bash
   jupyter notebook FDM_Implementations.ipynb
   ```

---

## Methodology

### von Neumann Stability Analysis

vNSA works by assuming the numerical error at each grid point takes the form of a Fourier mode:

$$\epsilon^n_j = G_k^n \, e^{ik(j\Delta x)}$$

Substituting this into the finite difference update equation and solving yields the **amplification factor** $G_k$. The scheme is stable if and only if:

$$|G_k| \leq 1 \quad \forall \, k$$

The polar decomposition $G_k = |G_k| e^{iφ_k}$ further reveals:
- **Dissipation** — whether $|G_k| < 1$ (amplitude decays artificially)
- **Dispersion** — whether $arg(G_k) ≠ 0$ (phase velocity is distorted)

### Initial Conditions Used

All schemes were tested against three initial conditions to probe different aspects of numerical behaviour:

- **Sine wave** $u(x, 0) = \sin(kx)$ — isolates the behaviour of a single Fourier mode
- **Gaussian-modulated sine** $u(x,0) = \exp(-(x-x_0)^2/\sigma^2) \sin(kx)$ — tests combined dispersion and dissipation for a localised wave packet
- **Heaviside step function** — tests how schemes handle discontinuities and high-frequency content

---

## Key Results

- The **FTCS scheme for the advection equation** is unconditionally unstable — its amplification factor always exceeds 1.
- The **Lax–Wendroff scheme** at λ = 1 is exactly non-dissipative, making it the most accurate advection scheme tested at the CFL limit.
- **Crank–Nicolson** for the heat equation achieves the best balance: unconditionally stable, second-order accurate in both space and time, and only mildly dissipative.
- All heat equation schemes studied are **non-dispersive** because their amplification factors are purely real.

---

## References

- R. J. LeVeque, *Finite Difference Methods for Ordinary and Partial Differential Equations*, SIAM, 2007
- R. R. Rosales, [Notes on von Neumann Stability Analysis](https://math.mit.edu/classes/18.300/Notes/Notes_vNSA.pdf), MIT 18.300
- K. K. Makwana, *Time Dependent PDEs – Computational Physics*
