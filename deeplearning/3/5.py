from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_product_mix", sense=LpMaximize)

x_A = LpVariable(name="x_A", lowBound=0, cat="Integer")  # x_A >= 0
x_B = LpVariable(name="x_B", lowBound=0, cat="Integer")  # x_B >= 0

#  20x_A + 50x_B
model += 20 * x_A + 50 * x_B, "Profit"

model += x_A >= 4 * x_B, "Sales_Ratio"  # x_A >= 4x_B
model += x_A <= 100, "Max_A"  # x_A <= 100
model += 2 * x_A + 4 * x_B <= 240, "Raw_Material"  # 2x_A + 4x_B <= 240

model.solve(PULP_CBC_CMD(msg=True))

optimal_x_A = x_A.varValue
optimal_x_B = x_B.varValue
optimal_profit = model.objective.value()

print(f"Оптимальное производство: A = {optimal_x_A:.0f}, B = {optimal_x_B:.0f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")
"""
❯ python deeplearning/4/5.py
Оптимальное производство: A = 80, B = 20
Максимальная прибыль: $2600.00
"""
