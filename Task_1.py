from pulp import LpMaximize, LpProblem, LpVariable

# Створення задачі лінійного програмування
model = LpProblem(name="optimization-production", sense=LpMaximize)

# Змінні: кількість "Лимонаду" та "Фруктового соку"
limonade = LpVariable(name="limonade", lowBound=0, cat="Continuous")
fruit_juice = LpVariable(name="fruit_juice", lowBound=0, cat="Continuous")

# Цільова функція: максимізація загальної кількості продуктів
model += limonade + fruit_juice, "Maximize total production"

# Обмеження ресурсів
model += 2 * limonade + 1 * fruit_juice <= 100, "Water" # Обмеження води
model += 1 * limonade <= 50, "Sugar" # Обмеження цукру
model += 1 * limonade <= 30, "Lemon juice constraint" # Обмеження лимонного соку
model += 2 * fruit_juice <= 40, "Fruit puree" # Обмеження фруктового пюре

# Розв'язання задачі
status = model.solve()

# Результати
print(f"Status: {model.status}")
print(f"Optimal production of Limonade: {limonade.value()} units")
print(f"Optimal production of Fruit Juice: {fruit_juice.value()} units")
print(f"Total production: {limonade.value() + fruit_juice.value()} units")