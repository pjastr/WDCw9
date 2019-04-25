import numpy as np

data = np.genfromtxt('jajka1.csv', delimiter=";", dtype=('|U16'))
data2 = np.array([[s.replace(',', '.') for s in line] for line in data], dtype=object)

row, col = data2.shape
suma = 0

for x in range(1, row):
    for y in range(1, col):
        if (data2[x][y] == ''):
            data2[x][y] = 0
        data2[x][y] = float(data2[x][y])
        suma += data2[x][y]

print("Średnia cena jaj to {}".format(suma / ((col - 1) * (row - 1))))

data3 = np.delete(data2, (0), axis=0)
data3 = np.delete(data3, 0, 1)

minimum = np.min(data3[np.nonzero(data3)])
maksimum = np.max(data3[np.nonzero(data3)])

ma = np.empty((0, 2))
mn = np.empty((0, 2))
for x in range(row):
    for y in range(col):
        if data2[x][y] == maksimum:
            ma = np.append(ma, [[data2[0][y], data2[x][0]]], axis=0)
        if data2[x][y] == minimum:
            mn = np.append(mn, [[data2[0][y], data2[x][0]]], axis=0)

print("\nNajdroższe jajka: ")
print(ma)
print("\nNajtańsze jajka: ")
print(mn)
