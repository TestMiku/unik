from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_course_allocation", sense=LpMaximize)

x_P = LpVariable(name="x_P", lowBound=0, cat="Integer")  # Практические курсы
x_H = LpVariable(name="x_H", lowBound=0, cat="Integer")  # Гуманитарные курсы

#  1500x_P + 1000x_H
model += 1500 * x_P + 1000 * x_H, "Revenue"

# Ограничения:
model += x_P + x_H == 30, "Total_Courses"  #  30 курсов
model += x_P >= 10, "Min_Practical"  # Минимум 10 практических
model += x_H >= 10, "Min_Humanistic"  # Минимум 10 гуманитарных

model.solve(PULP_CBC_CMD(msg=True))

optimal_x_P = x_P.varValue
optimal_x_H = x_H.varValue
optimal_revenue = model.objective.value()

print(f"Оптимальное распределение курсов: Практические = {optimal_x_P:.0f}, Гуманитарные = {optimal_x_H:.0f}")
print(f"Максимальный доход: ${optimal_revenue:.2f}")

"""
❯ python deeplearning/3/8.py
Оптимальное распределение курсов: Практические = 20, Гуманитарные = 10
Максимальный доход: $40000.00
"""

