is_number = False
number = 0
while not is_number:
    try:
        num = int(input("Adjon meg egy egész számot: "))
        is_number = True
    except ValueError:
        print("Ez nem egy egész szám.")
if num % 2 == 0:
    print("Páros.")
else:
    print("Páratlan.")

i = 1
while i <= 5:
    print(i, end=' ')
    i+=1
print("\n")
for j in range(100):
    print(j+1, end=' ')
print("\n")
for j in range(30, 44):
    print(j+1, end=' ')
print("\n")
for n in range(1, 100):
    if n % 2 == 1:
        print(n, end=" ")
