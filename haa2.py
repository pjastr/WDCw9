import numpy as np


def sredniacena(tabela):

    suma = 0
    a = 0

    for x in range(1, 17):
        for y in range(1, 9):
            if tabela[x][y] != '':
                suma += tabela[x][y].astype(np.float)
                a += 1

    suma = suma / a
    return suma


def taniedrogie(tabela):

    min = 50
    max = 0

    miasto1 = ''
    miasto2 = ''

    sklep1 = ''
    sklep2 = ''

    for x in range(1, 17):
        for y in range(1, 9):
            if tabela[x][y] != '':
                if tabela[x][y].astype(np.float) < min:
                    min = tabela[x][y].astype(np.float)
                    miasto1 = tabela[0][y]
                    sklep1 = tabela[x][0]
                if tabela[x][y].astype(np.float) > max:
                    max = tabela[x][y].astype(np.float)
                    miasto2 = tabela[0][y]
                    sklep2 = tabela[x][0]
    wynik = np.array([[miasto1, sklep1, min], [miasto2, sklep2, max]])
    return wynik


data = np.genfromtxt('jajka1.csv', delimiter=";", dtype='|U16')
data2 = np.array([[s.replace(',', '.') for s in line] for line in data])

print("Srednia cena jajek to: {}".format(sredniacena(data2)))
print(taniedrogie(data2))

