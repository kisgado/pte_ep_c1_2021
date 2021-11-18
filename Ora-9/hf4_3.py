is_number = False
while not is_number:
    try:
        n = int(input("Adja meg, a Pascal-háromszög sorainak számát: "))
        is_number = True
    except ValueError:
        print("Ez nem egy egész szám.")

matrix = [[1], [1, 1]]
for i in range(1, n):
    sor = [1] * (i+2)
    for j in range(1, i+1):
        sor[j] = matrix[i][j] + matrix[i][j-1]
    matrix.append(sor)

for i in range(n+1):
    for j in range(len(matrix[i])):
        print(str(matrix[i][j]), end='\t')
    print("")
