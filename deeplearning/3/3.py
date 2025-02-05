import numpy as np
from scipy.optimize import linprog

# z = 5x1 + 4x2
c = [-5, -4]  

# Базовые ограничения сырья M1 и M2:
A = [
    [2, 1],   # M1
    [1, 2]    # M2
]
b = [8, 6]  # Ограничения на количество сырья

def solve_lp(x1_bounds, x2_bounds, additional_constraints=None, additional_rhs=None):
    A_extended = A[:]
    b_extended = b[:]
    
    if additional_constraints is not None and additional_rhs is not None:
        A_extended.extend(additional_constraints)
        b_extended.extend(additional_rhs)
    
    result = linprog(c, A_ub=A_extended, b_ub=b_extended, bounds=[x1_bounds, x2_bounds], method='highs')

    if result.success:
        return f"Оптимальное решение: x1 = {result.x[0]:.2f}, x2 = {result.x[1]:.2f}, Прибыль: {-result.fun:.2f}"
    else:
        return "Решение не найдено"

# a) Ограничение x1 <= 2.5
solution_a = solve_lp((0, 2.5), (0, None))

# b) Ограничение x2 >= 2
solution_b = solve_lp((0, None), (2, None))

# c) Связь x2 = x1 + 1 -> заменяем x2 новой переменной x1 + 1
solution_c = solve_lp((0, None), (None, None), additional_constraints=[[-1, 1]], additional_rhs=[1])

# d) Увеличение сырья M1 >= 24
solution_d = solve_lp((0, None), (0, None), additional_constraints=[[2, 1]], additional_rhs=[24])

# e) Комбинация: M1 >= 24 и x2 >= x1 + 1
solution_e = solve_lp((0, None), (None, None), additional_constraints=[[2, 1], [-1, 1]], additional_rhs=[24, 1])

solutions = {
    "a) x1 <= 2.5": solution_a,
    "b) x2 >= 2": solution_b,
    "c) x2 = x1 + 1": solution_c,
    "d) M1 >= 24": solution_d,
    "e) M1 >= 24 и x2 >= x1 + 1": solution_e
}

for case, result in solutions.items():
    print(f"{case}: {result}")

"""
❯ python deeplearning/3/3.py
a) x1 <= 2.5: Оптимальное решение: x1 = 2.50, x2 = 1.75, Прибыль: 19.50
b) x2 >= 2: Оптимальное решение: x1 = 2.00, x2 = 2.00, Прибыль: 18.00
c) x2 = x1 + 1: Оптимальное решение: x1 = 3.33, x2 = 1.33, Прибыль: 22.00
d) M1 >= 24: Оптимальное решение: x1 = 3.33, x2 = 1.33, Прибыль: 22.00
e) M1 >= 24 и x2 >= x1 + 1: Оптимальное решение: x1 = 3.33, x2 = 1.33, Прибыль: 22.00

"""
