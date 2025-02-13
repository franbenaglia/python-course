from sympy.solvers import solve
from sympy import Symbol
x = Symbol('x')
res = solve(x**2 - 1, x)
print(res)