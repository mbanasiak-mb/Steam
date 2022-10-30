import re
import matplotlib.pyplot as plt
import numpy as np

from scipy.optimize import curve_fit

# --------------------------------------------------------------------------------


def func(px, a, b):
    return a ** px * b

# --------------------------------------------------------------------------------


pattern = re.compile('([0-9]+.[0-9]+)(?=( hrs on record))')

text = ''
with open('steam.txt', 'r') as f:
    text = f.read()


matches = re.findall(pattern=pattern, string=text)

py = []
for match in matches:
    val = float(match[0])
    py.append(val)


py.sort()
py = py[:-2]
px = range(0, len(py))

plt.semilogy(px, py, '.-k')

popt, _ = curve_fit(func, px, py)

a = popt[0]
b = popt[1]

tx = np.linspace(px[0], px[-1], px[-1] * 10)
ty = func(tx, a, b)

plt.plot(tx, ty, '-r')

print(a)
print(b)

# --------------------------------------------------------------------------------

plt.ylabel('hours')
plt.xlabel('n-th game')
plt.grid(True)

plt.show()
