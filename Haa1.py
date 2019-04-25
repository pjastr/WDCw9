import numpy as np

data = np.genfromtxt('jajka1.csv', delimiter=";", dtype=('|U16'))

data2 = np.array([[s.replace(',', '.') for s in line] for line in data])

suma = 0

x = 0

for i in range(1, 17):

    for j in range(1, 9):

        if data2[i][j] == "":

            data2[i][j] = 0

        suma += data2[i][j].astype(np.float)

        x += 1

srednia = suma / x

print('Średnia : ', srednia)

mini = 100

maxi = 0

m1 = ''

m2 = ''

s1 = ''

s2 = ''

for i in range(1, 17):

    for j in range(1, 9):

        if data2[i][j].astype(np.float) > maxi:

            maxi = data2[i][j].astype(np.float)

            m1 = data[0][j]

            s1 = data[i][0]

        if (data2[i][j].astype(np.float) < mini) and (data2[i][j].astype(np.float) != 0):

            mini = data2[i][j].astype(np.float)

            m2 = data[0][j]

            s2 = data[i][0]

x = np.array(['Miasto', 'Nazwa sieci', 'Ceny', m1, s1, maxi, m2, s2, mini])

x.resize(3, 3)

print(x)
