from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_production_mix", sense=LpMaximize)

x_S = LpVariable(name="x_S", lowBound=0, cat="Integer")  # Количество листов
x_B = LpVariable(name="x_B", lowBound=0, cat="Integer")  # Количество брусьев

#  40x_S + 35x_B
model += 40 * x_S + 35 * x_B, "Profit"

model += x_S <= 800, "Max_Sheets"  # Макс 800 листов
model += x_B <= 600, "Max_Bars"  # Макс 600 брусьев
model += x_S <= 550, "Demand_Sheets"  # Спрос на листы - 550
model += x_B <= 580, "Demand_Bars"  # Спрос на брусья - 580

model.solve(PULP_CBC_CMD(msg=True))

optimal_x_S = x_S.varValue
optimal_x_B = x_B.varValue
optimal_profit = model.objective.value()

print(f"Оптимальное производство: Листы = {optimal_x_S:.0f}, Брусья = {optimal_x_B:.0f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")
"""
❯ python deeplearning/3/6.py
Оптимальное производство: Листы = 550, Брусья = 580
Максимальная прибыль: $42300.00
"""
