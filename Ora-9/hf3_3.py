is_number = False
while not is_number:
    try:
        kor = int(input("Adja meg a korát: "))
        is_number = True
    except ValueError:
        print("Ez nem egy egész szám.")
nem = input("Adja meg a nemét (m / f): ")

if 10 <= kor <= 12 and nem == "f":
    print("Játszhat a csapatban.")
else:
    print("Nem játszhat a csapatban.")
# -----------------------------------------------------

nem = input("Adja meg a nemét (m / f): ")
is_number = False
while not is_number and nem == "f":
    try:
        kor = int(input("Adja meg a korát: "))
        is_number = True
    except ValueError:
        print("Ez nem egy egész szám.")
if 10 <= kor <= 12 and nem == "f":
    print("Játszhat a csapatban.")
else:
    print("Nem játszhat a csapatban.")