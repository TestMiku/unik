from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_hat_production", sense=LpMaximize)

x_1 = LpVariable(name="x_1", lowBound=0, upBound=150, cat="Integer")  # макс. 150
x_2 = LpVariable(name="x_2", lowBound=0, upBound=200, cat="Integer")  # макс. 200

# максимизация прибыли: 8x_1 + 5x_2
model += 8 * x_1 + 5 * x_2, "Profit"

#  400 Typов 2 шляпы
model += 2 * x_1 + x_2 <= 400, "Labor_Time"

model.solve(PULP_CBC_CMD(msg=True))

optimal_x_1 = x_1.varValue
optimal_x_2 = x_2.varValue
optimal_profit = model.objective.value()

print(f"Оптимальное производство: Шляпы типа 1 = {optimal_x_1:.0f}, Шляпы типа 2 = {optimal_x_2:.0f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")
"""
❯ python deeplearning/3/12.py
Оптимальное производство: Шляпы типа 1 = 100, Шляпы типа 2 = 200
Максимальная прибыль: $1800.00
"""
