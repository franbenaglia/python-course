from sympy import symbols, Eq, solve

x, y = symbols('x y')

eq1 = Eq(x + y, - 5)
eq2 = Eq(x - y, + 3)

sol_dict = solve((eq1,eq2), (x, y))

print(f'x = {sol_dict[x]}')
print(f'y = {sol_dict[y]}')