szamok = [6, 4, 5]

if szamok[0] >= szamok[1] and szamok[0] >= szamok[2]:
    ln = szamok[0]
    print("Az első szám a legnagyobb.")
elif szamok[1] >= szamok[0] and szamok[1] >= szamok[1]:
    ln = szamok[1]
    print("A második szám a legnagyobb.")
elif szamok[2] >= szamok[0] and szamok[2] >= szamok[1]:
    ln = szamok[2]
    print("A harmadik szám a legnagyobb.")

if szamok[0] <= szamok[1] and szamok[0] <= szamok[2]:
    lk = szamok[0]
    print("Az első szám a legkisebb.")
elif szamok[1] <= szamok[0] and szamok[1] <= szamok[1]:
    lk = szamok[1]
    print("A második szám a legkisebb.")
elif szamok[2] <= szamok[0] and szamok[2] <= szamok[1]:
    lk = szamok[2]
    print("A harmadik szám a legkisebb.")

for i in range(len(szamok)):
    if szamok[i] != lk and szamok[i] != ln:
        print("A(z)",i+1,". szám a középső.")
try:
    jegy = int(input("Osztályzat: "))
    if jegy == 1:
        print("elégtelen")
    elif jegy == 2:
        print("elégséges")
    elif jegy == 3:
        print("közepes")
    elif jegy == 4:
        print("jó")
    elif jegy == 5:
        print("jeles")
    else:
        print("Hibás érték.")
except ValueError:
    print("Nem számjegy a megadott érték.")

try:
    print(float(input("Szám: "))*3)
except ValueError:
    print("Nem szám.")

szam = input("Egész szám: ")
if szam.isnumeric():
    szam = int(szam)
    print(szam*3)
else:
    print("Nem szám")
