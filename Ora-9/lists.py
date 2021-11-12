lista = [1, 2.5, "alma", False]
print(len(lista))
print("típus:", type(len(lista)))
print("A 2 érték benne van-e a listában: ", 2 in lista)
print(" -||- típusa: ", type(2 in lista))

try:
    print("A 2.5 érték pozíciója a listában: ", lista.index(2.5))
except ValueError:
    print("A 2.5 érték nincs a listában.")
