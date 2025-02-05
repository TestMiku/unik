from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_production_chemicals", sense=LpMaximize)

x_A = LpVariable(name="x_A", lowBound=30, upBound=150, cat="Integer")  # A (30 <= A <= 150)
x_B = LpVariable(name="x_B", lowBound=40, upBound=200, cat="Integer")  # B (40 <= B <= 200)

# 8x_A + 10x_B
model += 8 * x_A + 10 * x_B, "Profit"

model += 0.5 * x_A + 0.5 * x_B <= 150, "Raw_Material_I"  # макс. 150 единиц
model += 0.6 * x_A + 0.4 * x_B <= 145, "Raw_Material_II"  # макс. 145 единиц

model.solve(PULP_CBC_CMD(msg=True))

optimal_x_A = x_A.varValue
optimal_x_B = x_B.varValue
optimal_profit = model.objective.value()

print(f"Оптимальное производство: Продукт A = {optimal_x_A:.0f}, Продукт B = {optimal_x_B:.0f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")


"""
❯ python deeplearning/3/9.py
Оптимальное производство: Продукт A = 101, Продукт B = 200
Максимальная прибыль: $2800.00
"""

