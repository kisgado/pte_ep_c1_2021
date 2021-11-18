is_number = False
while not is_number:
    try:
        elso = float(input("Adja meg a sorozat első elemét: "))
        is_number = True
    except ValueError:
        print("Ez nem egy szám.")

is_number = False
while not is_number:
    try:
        masodik = float(input("Adja meg a sorozat második elemét: "))
        is_number = True
    except ValueError:
        print("Ez nem egy szám.")

is_number = False
while not is_number:
    try:
        n = int(input("Adja meg, hogy a sorozat hányadik eleme érdekli: "))
        is_number = True
    except ValueError:
        print("Ez nem egy egész szám.")

q = masodik / elso
szam = elso * (q**(n-1))
print(szam)