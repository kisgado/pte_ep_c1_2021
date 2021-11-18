print("Szorzótábla (10x10)")
meret = 10
szorzotabla = [[0] * meret] * meret
for i in range(meret):
    for j in range(meret):
        szorzotabla[i][j] = (i+1)*(j+1)
        if j == 9:
            print(szorzotabla[i][j])
        else:
            print(szorzotabla[i][j], end="\t")
