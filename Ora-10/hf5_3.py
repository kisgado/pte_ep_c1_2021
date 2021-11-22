is_number = False
while not is_number:
    try:
        szam = int(input("Adjon meg egy számot: "))
        is_number = True
    except ValueError:
        print("Ez nem egy egész szám.")
print(f"A megadott szám (decimális): {szam}")
print(f"A megadott szám (bináris): {szam:b}")
print(f"A megadott szám (oktális): {szam:o}")
print(f"A megadott szám (hexadecimális): {szam:x}")
