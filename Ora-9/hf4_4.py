szoveg = input("Adjon meg egy szöveget: ").lower().replace(" ", "")
palindrom = True
for i in range(len(szoveg)):
    if szoveg[-1 - i] != szoveg[i]:
        palindrom = False
print("A megadott szöveg palindrom.") if palindrom == True else print("A megadott szöveg nem palindrom.")
