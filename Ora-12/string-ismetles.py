def feladat(szam):
    print("\n" + str(szam) + ". feladat")


print("String ismétlés")


def elso():
    feladat(1)
    szoveg = "asdfghfjafk"
    karakter = "f"

    def megtalal(szoveg, karakter) -> list/int:
        """
        Karakter pozícióinak megkeresése.
        :param szoveg: amiben keressük a karaktert
        :param karakter: egy karakter, amit keresünk
        :return: karakter előfordulásai, vagy -1 ha nincs benne
        """
        helyek = []
        for i in range(len(szoveg)):
            if szoveg[i] == karakter:
                helyek.append(i)
        if len(helyek) == 0:
            return -1
        return helyek

    print(megtalal(szoveg, karakter))


def masodik():
    feladat(2)
    prefixes = "JKLMNOPQ"
    suffix = "ack"
    for elem in prefixes:
        print(elem + suffix)


elso()
masodik()
