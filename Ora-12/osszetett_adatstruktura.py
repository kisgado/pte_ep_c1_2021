my_str = ""
my_list = []
my_touple = ()
my_dict = {}

my_touple = (31, 43, 456, 67, 89, 543, 42)
print(my_touple)
print(len(my_touple))

my_dict["kulcs"] = "Érték"
my_dict["lista"] = [10, 32, 11]
my_dict["alma"] = "apple", "Apfel"

print(my_dict)
print(len(my_dict))


def beolvasas(filepath: str):
    szinek = {}
    fileobject = open(filepath, "r")
    for row in fileobject:
        row_datas = row.strip().split("\t")
        szinek[row_datas[1]] = (row_datas[3], row_datas[4], row_datas[5])
    fileobject.close()
    return szinek


szin_szotar = beolvasas("color.csv")
print(szin_szotar["Narancs"])
print(szin_szotar.get("kutya", "Nincs ilyen szín."))
print("Narancs" in szin_szotar)
print(szin_szotar.keys())
print(szin_szotar.values())

szin_szotar2 = szin_szotar.copy()
szin_szotar3 = szin_szotar
del(szin_szotar2["Narancs"])
szin_szotar.clear()
# Ha lista, szótár az adattípus akkor .copy() a másolat, különben "ugyanaz" lesz
print(len(szin_szotar3), len(szin_szotar2), len(szin_szotar))
