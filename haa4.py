import numpy as np


def srednia(tabelka):
    suma = 0
    a = 0
    for x in range(1, 17):
        for y in range(1, 9):
            if tabelka[x][y] != '':
                suma += tabelka[x][y].astype(np.float)
                a += 1
    print(suma / a)


def taniedrogie(tabelka):
    m = 50
    d = 0
    miasto1 = ''
    miasto2 = ''
    siec1 = ''
    siec2 = ''
    for x in range(1, 17):
        for y in range(1, 9):
            if tabelka[x][y] != '':
                if tabelka[x][y].astype(np.float) < m:
                    m = tabelka[x][y].astype(np.float)
                    miasto1 = tabelka[0][y]
                    siec1 = tabelka[x][0]
                if tabelka[x][y].astype(np.float) > d:
                    d = tabelka[x][y].astype(np.float)
                    miasto2 = tabelka[0][y]
                    siec2 = tabelka[x][0]
    wynik = np.array([[miasto1, siec1, m], [miasto2, siec2, d]])
    return wynik


data = np.genfromtxt('jajka1.csv', delimiter=";", dtype='|U16')
data2 = np.array([[s.replace(',', '.') for s in line] for line in data])

srednia(data2)
print(taniedrogie(data2))
