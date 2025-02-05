from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_shelf_allocation", sense=LpMaximize)

x_G = LpVariable(name="x_G", lowBound=0, upBound=200, cat="Integer")  # макс. 200
x_W = LpVariable(name="x_W", lowBound=0, upBound=120, cat="Integer")  # макс. 120

# 1.00x_G + 1.35x_W
model += 1.00 * x_G + 1.35 * x_W, "Profit"

# общая площадь ≤ 60 ft^2
model += 0.2 * x_G + 0.4 * x_W <= 60, "Shelf_Space"

model.solve(PULP_CBC_CMD(msg=True))

optimal_x_G = x_G.varValue
optimal_x_W = x_W.varValue
optimal_profit = model.objective.value()

print(f"Оптимальное размещение: Grano = {optimal_x_G:.0f} коробок, Wheatie = {optimal_x_W:.0f} коробок")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")


"""
❯ python deeplearning/3/10.py
Оптимальное размещение: Grano = 200 коробок, Wheatie = 50 коробок
Максимальная прибыль: $267.50
"""
