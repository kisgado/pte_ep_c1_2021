import random


def feladat(n):
    print("\n%d. feladat" % n)


feladat(4)
lista = []
be = input("Adjon meg egy értéket: ")
while be!="":
    lista.append(be)
    be = input("Adjon meg egy értéket: ")
for elem in lista:
    print(elem, end=" | ")


def maximum_kereses(max_lista: list[float]) -> float:
    """
    Megkeresi egy valós számokat tartalmazó listának a legnagyobb elemét.
    :param max_lista:
    :return:
    """
    max = max_lista[0]
    for number in max_lista:
        if max < number:
            max = number
    return max

def kiiratas(szam: float):
    print(szam)

feladat(5)
lista = []
for i in range(20):
    lista.append(random.randint(0, 100))
minimum = lista[0]
maximum = lista[0]
for i in range(len(lista)):
    print(lista[i], end=" ")
    if lista[i] > maximum:
        maximum = lista[i]
    elif lista[i] < minimum:
        minimum = lista[i]
print("\nMinimum:", minimum)
print("Maximum:", maximum)
kiiratas(maximum_kereses(lista))


feladat(6)
nev = input("Adja meg a nevét: ")
nem = input("Adja meg a nemét (f / n): ")

if nem == "f":
    print(nev, "Úr")
elif nem == "n":
    print(nev, "Asszony")
