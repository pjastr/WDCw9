import numpy as np
data = np.genfromtxt('jajka1.csv', delimiter=";", dtype='|U16')
datarepl = np.array([[s.replace(',', '.') for s in line] for line in data])
suma = 0
x = 0
for i in range(1, int(datarepl.size / datarepl[0].size)):
    for j in range(1, datarepl[0].size):
        if datarepl[i, j] == "":
            datarepl[i, j] = 0
        suma = suma + datarepl[i, j].astype('float64')
        x += 1
print("Średnia = {}".format(suma / x))
miastomaksimum = ""
miastominimum = ""
sklepmaksimum = ""
sklepminimum = ""
minimum = datarepl[1, 1].astype('float64')
maksimum = datarepl[1, 1].astype('float64')
for i in range(1, int(datarepl.size / datarepl[0].size)):
    for j in range(1, datarepl[0].size):
        if datarepl[i, j].astype('float64') != 0:
            if datarepl[i, j].astype('float64') > maksimum:
                maksimum = datarepl[i, j].astype('float64')
                miastomaksimum = datarepl[0, j]
                sklepmaksimum = datarepl[i, 0]
            if datarepl[i, j].astype('float64') < minimum:
                minimum = datarepl[i, j].astype('float64')
                miastominimum = datarepl[0, j]
                sklepminimum = datarepl[i, 0]
x = np.array([['Miasto', 'Nazwa sieci', 'Ceny'],
              [miastomaksimum, sklepmaksimum, maksimum],
              [miastominimum, sklepminimum, minimum]])
print(x)