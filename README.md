# Comparison of Stability of PDE Solvers - Von Neumann Analysis

### The Sample Problem - for the Linear Advection Equation FDM Solvers:

$$ \frac{ \partial f} {\partial t} +  \frac{\partial f}{ \partial x} = 0 $$
In the domain  $ x \in [0, 10] $ with the initial conditions as a Gaussian Modulated Sine Wave with mean 5, variance 1:
$$ f(x, 0) = \text{exp} \left[\frac{- (x - 5)^2}{2}\right]  \sin{(kx)} $$
At varying wave numbers 'k'


We examine the Growth Factor till time $t = 2$ for each Finite Difference Method