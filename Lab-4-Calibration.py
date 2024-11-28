import numpy as np
from matplotlib import pyplot as plt


def MNK(x, y):
    x = np.array(x)
    y = np.array(y)
    A = np.vstack([x, np.ones(len(x))]).T
    k, b = np.linalg.lstsq(A, y, rcond=None)[0]

    residuals = y - (k * x + b)
    sse = np.sum(residuals ** 2)
    sst = np.sum((y - np.mean(y)) ** 2)
    r2 = 1 - (sse / sst)
    var_k = (sse / (len(x) - 2)) / np.sum((x - np.mean(x)) ** 2)
    sig_k = np.sqrt(var_k)

    print(f"Slope (k): {k:.4f}, Standard Error (sig_k): {sig_k:.4f}, Intercept (b): {b:.4f}")
    return k, sig_k, b


name40 = '35-1.txt'
name60 = '40-1.txt'
name80 = '60-1.txt'
name100 = '80-1.txt'
name120 = '100-1.txt'

Sred40 = 0
Sred60 = 0
Sred80 = 0
Sred100 = 0
Sred120 = 0

V40, V60, V80, V100, V120 = 0, 0, 0, 0, 0

filenames = [name40, name60, name80, name100, name120]
sred = []
mm = [35, 40, 60, 80, 100]

for i, filename in enumerate(filenames):
    try:
        with open(filename, 'r') as file:
            V = float(file.readline())
            Sred = 0
            for l in range(100):
                try:
                    Sred += float(file.readline())
                except ValueError as e:
                    print(f"Error reading data from {filename}: {e}. Skipping this line")
                    continue
            Sred /= 100
            sred.append(Sred)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

plt.scatter(sred, mm, c=['red', 'blue', 'green', 'black', 'orange'])

k, sig_k, b = MNK(sred, mm)

x_plot = np.linspace(min(sred), max(sred), 100)
y_plot = k * x_plot + b
plt.plot(x_plot, y_plot, c='purple', label=f"k = {k:.4f}, b = {b:.4f}")

print("Coefficient of conversion of voltage to mm k_0 =", 1 / k)

plt.xlabel("Average Voltage (V)")
plt.ylabel("Thickness (mm)")
plt.legend()
plt.grid(True)
plt.show()

