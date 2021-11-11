import math
pontok=[]
print("P(x1,y1), Q(x2,y2)")
pontok.append(int(input("x1: ")))
pontok.append(int(input("x2: ")))
pontok.append(int(input("y1: ")))
pontok.append(int(input("y2: ")))

d = math.sqrt((pontok[2]-pontok[0])**2+(pontok[3]-pontok[1])**2)

print("A megadott pontok távolsága: ", d)
