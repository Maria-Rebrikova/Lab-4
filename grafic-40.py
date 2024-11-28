import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из файла (предполагается, что данные находятся в файле 'data.txt',
# каждое значение напряжения на новой строке)
try:
    voltage_data = np.loadtxt('40-spusk.txt')
except FileNotFoundError:
    print("Файл 'data.txt' не найден. Убедитесь, что файл существует и находится в той же директории, что и скрипт.")
    exit()


# Параметры эксперимента
num_points = len(voltage_data)
experiment_duration = 20  # секунды
conversion_factor = 0.55  # коэффициент преобразования напряжения в высоту

# Вычисление высоты уровня воды
water_height = voltage_data * conversion_factor

# Вычисление времени для каждой точки данных
time = np.linspace(0, experiment_duration, num_points)

# Построение графика
plt.figure(figsize=(10, 6))  # Увеличим размер графика для лучшей читаемости
plt.plot(time, water_height)
plt.xlabel("Время (с)")
plt.ylabel("Высота уровня воды (м)")
plt.title("Зависимость высоты уровня воды от времени")
plt.grid(True)
plt.show()


# Дополнительная обработка данных (опционально):
# Можно добавить вычисление средней высоты, стандартного отклонения и т.д.
average_height = np.mean(water_height)
std_height = np.std(water_height)
print(f"Средняя высота уровня воды: {average_height:.2f}")
print(f"Стандартное отклонение высоты уровня воды: {std_height:.2f}")

