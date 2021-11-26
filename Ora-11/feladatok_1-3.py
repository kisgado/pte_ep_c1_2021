import math
import random


def feladat(n):
    print("%d. feladat" % n)


# 1. program: km/h -> m/s
feladat(1)
kmph = float(input("Adja meg a sebességet (km/h): "))
print(kmph * 3.6)

# 2. program: véletlen egész számok lista --> páros és páratlan
feladat(2)
veletlen = []
paros = []
paratlan = []
darab = 100
for i in range(darab):
    veletlen.append(random.randint(0, 100))
for i in range(len(veletlen)):
    if veletlen[i] % 2 == 0:
        paros.append(veletlen[i])
    elif veletlen[i] % 2 == 1:
        paratlan.append(veletlen[i])
print("\nPáros számok:")
for elem in paros:
    print(elem, end=" ")
print("\n\nPáratlan számok:")
for elem in paratlan:
    print(elem, end=" ")

# 3. program: bekért oldalhosszakból 3szög kerület, terület
feladat(3)
a = int(input("\nAdja meg a háromszög első oldalát: "))
b = int(input("Adja meg a háromszög második oldalát: "))
c = int(input("Adja meg a háromszög harmadik oldalát: "))

ker = a + b + c
d = (a + b + c) / 2
ter = math.sqrt(d * (d - a) * (d - b) * (d - c))

print("\nA háromszög kerülete:", ker)
print("A háromszög területe:", ter)
