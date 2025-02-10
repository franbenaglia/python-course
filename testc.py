import sympy as sp
x = sp.symbols('x')
f = x**2 + 3*x + 5
f_prime = sp.diff(f, x)
print(f"The derivative of f(x) is: {f_prime}")
