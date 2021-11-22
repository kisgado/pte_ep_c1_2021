import math
szamok = [0, 0, 0]
for i in range(3):
    is_number = False
    while not is_number:
        try:
            szamok[i] = int(input("Adjon meg egy számot: "))
            is_number = True
        except ValueError:
            print("Ez nem egy egész szám.")

a = szamok[0]
b = szamok[1]
c = szamok[2]

try:
    x1 = (-b + math.sqrt((b * b) - (4 * a * c))) / (2 * a)
except ValueError:
    print("x1 nem értelmezhető a valós számok halmazán.")
try:
    x2 = (-b - math.sqrt((b * b) - (4 * a * c))) / (2 * a)
except ValueError:
    print("x2 nem értelmezhető a valós számok halmazán.")
if x1 == x2:
    print("x1 =", x1)
else:
    print("x1 =", x1)
    print("x2 =", x2)
