ki = open("szorzotabla.txt", "w")
meret = 10
szorzotabla = [[0] * meret] * meret
for i in range(meret):
    for j in range(meret):
        szorzotabla[i][j] = (i+1)*(j+1)
        if j == 9:
            sor = str(szorzotabla[i][j])+"\n"
            ki.write(sor)
        else:
            sor = str(szorzotabla[i][j]) + "\t"
            ki.write(sor)
