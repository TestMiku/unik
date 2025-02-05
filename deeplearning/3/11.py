from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="jack_time_allocation", sense=LpMaximize)

work = LpVariable(name="work", lowBound=0, cat="Continuous")  # Часы на работу
play = LpVariable(name="play", lowBound=0, upBound=4, cat="Continuous")  # Часы на игру (макс. 4)

model += 1 * work + 2 * play, "Pleasure"

model += work + play == 10, "Total_Time"  # Всего 10 часов
model += work >= play, "Work_At_Least_Play"  # Учёбы не меньше, чем игры

model.solve(PULP_CBC_CMD(msg=True))

optimal_work = work.varValue
optimal_play = play.varValue
optimal_pleasure = model.objective.value()

print(f"Оптимальное распределение времени: Работа = {optimal_work:.2f} часов, Игра = {optimal_play:.2f} часов")
print(f"Максимальное удовольствие: {optimal_pleasure:.2f}")
"""
❯ python deeplearning/3/11.py
Оптимальное распределение времени: Работа = 6.00 часов, Игра = 4.00 часов
Максимальное удовольствие: 14.00
"""
