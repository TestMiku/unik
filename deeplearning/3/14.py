from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_coal_mixing", sense=LpMaximize)

# доля использования углей C1 и C2
x_C1 = LpVariable(name="x_C1", lowBound=0, cat="Continuous")  # Доля угля C1
x_C2 = LpVariable(name="x_C2", lowBound=0, cat="Continuous")  # Доля угля C2

# максимизация выработки пара: 12000 * x_C1 + 9000 * x_C2
model += 12000 * x_C1 + 9000 * x_C2, "Steam_Production"

# 100% смеси
model += x_C1 + x_C2 == 1, "Mixing_Proportion"

# взвешенное среднее не должно превышать 2000 ppm
model += 1800 * x_C1 + 2100 * x_C2 <= 2000, "Sulfur_Limit"

# взвешенное среднее не должно превышать 20 lb/hr
model += 2.1 * x_C1 + 0.9 * x_C2 <= 20, "Smoke_Limit"

model.solve(PULP_CBC_CMD(msg=True))

optimal_x_C1 = x_C1.varValue
optimal_x_C2 = x_C2.varValue
optimal_steam = model.objective.value()

print(f"Оптимальное соотношение углей: C1 = {optimal_x_C1:.2f}, C2 = {optimal_x_C2:.2f}")
print(f"Максимальное производство пара: {optimal_steam:.2f} lb/hr")
"""
❯ python deeplearning/3/14.py
Оптимальное соотношение углей: C1 = 1.00, C2 = 0.00
Максимальное производство пара: 12000.00 lb/hr
"""
