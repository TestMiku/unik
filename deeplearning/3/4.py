from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="product-mix", sense=LpMaximize)

x1 = LpVariable(name="x1", lowBound=0, cat="Integer")
x2 = LpVariable(name="x2", lowBound=0, cat="Integer")

# Функция прибыли
model += 2*x1 + 3*x2, "Profit"

# Ограничения по процессам
model += (10*x1 + 5*x2 <= 600), "Process_1"
model += (6*x1 + 20*x2 <= 600), "Process_2"
model += (8*x1 + 10*x2 <= 600), "Process_3"

model.solve(PULP_CBC_CMD(msg=False))

print(f"Оптимальный выпуск: x1 = {x1.varValue}, x2 = {x2.varValue}")
print(f"Максимальная прибыль: {model.objective.value()}")

"""
❯ python deeplearning/3/4.py
Оптимальный выпуск: x1 = 53.0, x2 = 14.0
Максимальная прибыль: 148.0
"""
