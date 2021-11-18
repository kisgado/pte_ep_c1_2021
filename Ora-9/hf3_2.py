is_number = False
while not is_number:
    try:
        num = int(input("Adja meg a termék árát (egész szám): "))
        is_number = True
    except ValueError:
        print("Ez nem egy egész szám.")

if (num < 10000):
    print("A termékre %d ft kedvezmény vonatkozik, így az ára %d ft." % (num * 0.1, num * 0.9))
else:
    print("A termékre %d ft kedvezmény vonatkozik, így az ára %d ft." % (num * 0.2, num * 0.8))
