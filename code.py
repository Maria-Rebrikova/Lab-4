import matplotlib.pyplot as plt
import numpy as np

def plot_height_vs_time_no_time(filename, calibration_coefficient, marker='.', linestyle=''):
    """Обработка файла только с высотами, с возможностью выбора маркеров и стиля линии."""
    try:
        heights = []
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                line = line.strip()
                if not line:
                    continue
                try:
                    height = float(line)
                    heights.append(height)
                except ValueError:
                    print(f"Ошибка в строке {line_num}: Не удалось преобразовать в число. Строка: '{line}'")
                    continue

        if not heights:
            raise ValueError("Файл пуст или содержит только некорректные данные.")

        heights = np.array(heights)
        time = np.arange(len(heights)) * 0.01 # Предполагаем шаг 0.01 сек

        calibrated_heights = heights * calibration_coefficient
        calibrated_heights = np.clip(calibrated_heights, 0, 120)

        plt.plot(time, calibrated_heights, marker=marker, linestyle=linestyle) # Изменения здесь
        plt.xlabel("Номер измерения")
        plt.ylabel("Высота (калиброванная, мм)")
        plt.title("Зависимость высоты от номера измерения")
        plt.grid(True)
        plt.show()

    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

if __name__ == "__main__":
    filename = input("Введите имя файла: ")
    try:
        calibration_coeff = float(input("Введите коэффициент калибровки: "))
        plot_height_vs_time_no_time(filename, calibration_coeff) # Используем значения по умолчанию для marker и linestyle
    except ValueError:
        print("Некорректный ввод коэффициента калибровки.")

