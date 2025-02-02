import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Метод Монте-Карло для обчислення інтегралу
def monte_carlo_integral(func, a, b, num_samples=10000):
    x_random = np.random.uniform(a, b, num_samples)
    y_random = func(x_random)
    integral = (b - a) * np.mean(y_random)
    return integral

# Різні кількості точок для перевірки
num_samples_list = [100, 1000, 10000, 100000, 1000000]

# Результати методу Монте-Карло для різних num_samples
print("Результати методу Монте-Карло для різної кількості точок:")
for num_samples in num_samples_list:
    monte_carlo_result = monte_carlo_integral(f, a, b, num_samples=num_samples)
    print(f"Кількість точок: {num_samples}, Інтеграл: {monte_carlo_result}")

# Перевірка результату за допомогою функції quad
quad_result, quad_error = spi.quad(f, a, b)
print("\nІнтеграл за допомогою quad: ", quad_result, "з помилкою", quad_error)

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()