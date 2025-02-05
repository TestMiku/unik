from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_weekly_production", sense=LpMaximize)

# количество произведенных рубашек и блузок)
shirts = LpVariable(name="shirts", lowBound=0, cat="Integer")  # Количество рубашек
blouses = LpVariable(name="blouses", lowBound=0, cat="Integer")  # Количество блузок

# Количество рабочих минут в каждом отделе
cutting_time = 25 * 8 * 5 * 60  # 25 рабочих, 8 часов в день, 5 дней в неделю
sewing_time = 35 * 8 * 5 * 60  # 35 рабочих, 8 часов в день, 5 дней в неделю
packaging_time = 5 * 8 * 5 * 60  # 5 рабочих, 8 часов в день, 5 дней в неделю

model += 8 * shirts + 12 * blouses, "Profit"

model += 20 * shirts + 60 * blouses <= cutting_time, "Cutting_Capacity"
model += 70 * shirts + 60 * blouses <= sewing_time, "Sewing_Capacity"
model += 12 * shirts + 4 * blouses <= packaging_time, "Packaging_Capacity"

model.solve(PULP_CBC_CMD(msg=True))

optimal_shirts = shirts.varValue
optimal_blouses = blouses.varValue
optimal_profit = model.objective.value()

print(f"Оптимальный выпуск продукции: Рубашки = {optimal_shirts:.0f}, Блузки = {optimal_blouses:.0f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")
"""
❯ python deeplearning/4/16.py
Оптимальный выпуск продукции: Рубашки = 480, Блузки = 840
Максимальная прибыль: $13920.00
"""
