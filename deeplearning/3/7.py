from pulp import LpMaximize, LpProblem, LpVariable, PULP_CBC_CMD

model = LpProblem(name="optimal_investment_allocation", sense=LpMaximize)

# Определяем переменные (инвестированные суммы в A и B)
x_A = LpVariable(name="x_A", lowBound=0, cat="Continuous")  # Инвестиция в A
x_B = LpVariable(name="x_B", lowBound=0, cat="Continuous")  # Инвестиция в B

# Целевая функция (максимизация прибыли: 0.05x_A + 0.08x_B)
model += 0.05 * x_A + 0.08 * x_B, "Profit"

# Ограничения:
model += x_A + x_B == 5000, "Total_Capital"  # Общий бюджет
model += x_A >= 1250, "Min_A"  # Минимум 25% в A
model += x_B <= 2500, "Max_B"  # Максимум 50% в B
model += x_A >= 0.5 * x_B, "A_at_least_half_B"  # A >= 0.5 * B

# Решение задачи с решателем CBC
model.solve(PULP_CBC_CMD(msg=True))

# Получение и вывод результатов
optimal_x_A = x_A.varValue
optimal_x_B = x_B.varValue
optimal_profit = model.objective.value()

print(f"Оптимальное распределение: Инвестиция A = ${optimal_x_A:.2f}, Инвестиция B = ${optimal_x_B:.2f}")
print(f"Максимальная прибыль: ${optimal_profit:.2f}")
"""
❯ python deeplearning/3/7.py
Оптимальное распределение: Инвестиция A = $2500.00, Инвестиция B = $2500.00
Максимальная прибыль: $325.00
"""
