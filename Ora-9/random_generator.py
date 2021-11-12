import random

r = random.random()
print(r)

print(random.randint(0,100))

a = random.randint(-100,100)
if a>0:
    print("A szám pozitív.")
elif a<0:
    print("A szám negatív.")
else:
    print("A szám 0.")