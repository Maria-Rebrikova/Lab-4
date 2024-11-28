import numpy as np

def calculate_calibration_factor(filename, height):
    """Вычисляет коэффициент калибровки из данных в файле."""
    try:
        with open(filename, 'r') as f:
            data = [float(line.strip()) for line in f]
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return None
    except ValueError:
        print(f"Ошибка: некорректные данные в файле '{filename}'.")
        return None

    if not data:  # проверка на пустой список
        print(f"Ошибка: файл '{filename}' пуст.")
        return None


    average_data = np.mean(data)
    if average_data == 0:
        print("Ошибка: среднее значение данных равно нулю. Невозможно вычислить коэффициент.")
        return None

    calibration_factor = height / average_data
    return calibration_factor


if __name__ == "__main__":
    filename = input("Введите имя файла: ")
    try:
        height = float(input("Введите значение высоты: "))
    except ValueError:
        print("Ошибка: некорректное значение высоты.")
        exit()

    calibration_factor = calculate_calibration_factor(filename, height)

    if calibration_factor is not None:
        print(f"Коэффициент калибровки: {calibration_factor:.4f}")

