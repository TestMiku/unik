from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_advertising_allocation", sense=LpMaximize)

#количество минут рекламы на радио и ТВ
radio = LpVariable(name="radio", lowBound=0, upBound=400, cat="Continuous")  # макс. 400
tv = LpVariable(name="tv", lowBound=0, cat="Continuous")  # Минуты рекламы на ТВ

# ТВ в 25 раз эффективнее радио
model += 1 * radio + 25 * tv, "Effectiveness"

# максимум $10,000
model += 15 * radio + 300 * tv <= 10000, "Budget"

model += radio >= 2 * tv, "Radio_at_least_2x_TV"

model.solve(PULP_CBC_CMD(msg=True))

optimal_radio = radio.varValue
optimal_tv = tv.varValue
optimal_effectiveness = model.objective.value()

print(f"Оптимальное распределение: Радио = {optimal_radio:.2f} минут, ТВ = {optimal_tv:.2f} минут")
print(f"Максимальная эффективность: {optimal_effectiveness:.2f}")

"""
❯ python deeplearning/3/13.py
Оптимальное распределение: Радио = 60.61 минут, ТВ = 30.30 минут
Максимальная эффективность: 818.18
"""
