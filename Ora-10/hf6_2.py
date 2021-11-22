szoveg = list(input("Adjon meg egy szöveget: "))
ujszoveg = szoveg

for i in range(len(szoveg)):
    if szoveg[i].islower():
        ujszoveg[i] = szoveg[i].upper()
    elif szoveg[i].isupper():
        ujszoveg[i] = szoveg[i].lower()
for betu in ujszoveg:
    print(betu, end="")