import RPi.GPIO as gpio
import sys
from time import sleep, time
from matplotlib import pyplot
import os

gpio.setmode(gpio.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
comp = 4
knop_out = 2
knop_in = 22
gpio.setup(knop_out, gpio.OUT, initial=gpio.HIGH)
gpio.setup(knop_in, gpio.IN)
gpio.setup(dac, gpio.OUT)
gpio.setup(comp, gpio.IN)


def perev(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]


def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2 * i  # Исправлено: добавлено *
        gpio.output(dac, perev(k))
        sleep(0.005)
        if gpio.input(comp) == 0:
            k -= 2 * i  # Исправлено: добавлено *
    return k


def waitForOpen():
    print('GPIO initialized. Wait for door opening...')
    while gpio.input(knop_in) > 0:
        sleep(0.1) # небольшая пауза, чтобы не перегружать процессор
    print('The door is open. Start sampling...')


volt = []
time_start = 0
time_len = 0
sampling_duration = 10 # секунды

try:
    waitForOpen()
    time_start = time.time()
    end_time = time_start + sampling_duration
    while time.time() < end_time:
        volt.append(adc() / 256 * 3.3)

except KeyboardInterrupt:
    print("Измерение прервано пользователем.")
except Exception as e:
    print(f"Произошла ошибка: {e}")


finally:
    time_len = time.time() - time_start
    filename = 'wave-data-120mm-kalibr.txt'
    if os.path.exists(filename):
        print(f"Внимание: файл '{filename}' уже существует. Данные будут перезаписаны.")
    with open(filename, 'w') as file:
        file.write(str(time_len) + '\n')
        for i in volt:
            file.write(str(i) + '\n')

    time_step = [i * time_len / len(volt) for i in range(len(volt))]
    pyplot.plot(time_step, volt)
    pyplot.xlabel("Время, с")
    pyplot.ylabel("Напряжение, В")
    pyplot.title("Зависимость напряжения от времени")
    pyplot.grid(True)
    pyplot.show()
    gpio.output(dac, 0)
    gpio.cleanup()
