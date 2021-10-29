"""
Többsoros komment
"""
#Egysoros komment

python = "python"
print("A python szó első karaktere:",python[0])
print("A python szó utolsó karaktere:",python[-1])
print("A python szó utolsó karaktere:",python[len(python)-1])

for i in range(len(python)):
    print(python[i],end=" ")

print("A python változó ötször:",python*5)
str2 = "hallgató"
str3 = "Hiába a hegynyi anyag, a hallgató gyorsan halad."
print(str2 in str3)
print(python in str3)
print(python not in str3)
print(str3[0:5])
print(str3[0:2]+str3[3:5])
print(str3[6:15])
print(python, str2, str3)
print(python, str2, str3, sep=" - ")
str4 = "HALLGATÓ"
print(str4, str4.lower())
print(str4 in str3)
print(str4.lower() in str3)