from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_advertising_allocation", sense=LpMaximize)

#количество рекламных объявлений на радио и ТВ
radio = LpVariable(name="radio", lowBound=1, cat="Integer")  # Минимум 1 радио реклама
tv = LpVariable(name="tv", lowBound=1, cat="Integer")  # Минимум 1 ТВ реклама

#максимизация охвата аудитории
model += (5000 + 2000 * (radio - 1)) + (4500 + 3000 * (tv - 1)), "Audience_Reach"

# $20,000
model += 300 * radio + 2000 * tv <= 20000, "Budget"

model += 300 * radio <= 0.8 * 20000, "Max_Radio_Budget"
model += 2000 * tv <= 0.8 * 20000, "Max_TV_Budget"

model.solve(PULP_CBC_CMD(msg=True))

optimal_radio = radio.varValue
optimal_tv = tv.varValue
optimal_reach = model.objective.value()

print(f"Оптимальное распределение: Радио = {optimal_radio:.0f} реклам, ТВ = {optimal_tv:.0f} реклам")
print(f"Максимальный охват аудитории: {optimal_reach:.0f} человек")
"""
❯ python deeplearning/3/15.py
оптимальное распределение: радио = 53 реклам, тв = 2 реклам
Максимальный охват аудитории: 116500 человек
"""
