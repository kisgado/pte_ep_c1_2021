f = open("teszt.txt", "r", encoding="utf-8")
sor = 0
karakter = 0
for line in f:
    sor += 1
    print(line, end="")
    for char in line:
        karakter +=1

print("A fileban {} db karakter található.".format(karakter))
print("A fileban {} db sor található.".format(sor))