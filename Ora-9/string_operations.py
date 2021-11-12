str1 = "Az almafán almák teremnek."
print("A szöveg hossza:", len(str1))
print(type(len(str1)))

str2 = "Terem"
str3 = str2.lower()
print(str1.find(str2))
print(str1.find(str3))
print(str3.islower())
print(str2.islower())
print(str2.upper())
print(str1.lower())
print(str2.isalpha())
print(str1.isalpha())   #szóköz, pont miatt hamis
print(str2.isalnum())
print(str1.isalnum())
str4 = "user123"
print(str4.isalpha())
print(str4.isalnum())
