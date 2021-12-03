def menu_opciok():
    print("Válasszon az alábbiak körül:\n\t0 - Kilépés\n\t1 - Új fa hozzáadása\n\t2 - Fajta lekérdezése")


def egesz_szam_bekerese(koordinata: str):
    szam = ""
    while szam == "":
        try:
            szam = int(input("Adjon meg %s koordinátát: " % koordinata))
        except ValueError:
            print("Nem egész szám.")
    return szam


def uj_fa():
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely in fak:
        print("Itt már van egy fa.")
    else:
        fak[hely] = input("Adja meg a fa fajtáját: ")
        print("Sikeresen rögzítve.")


def szotar_kiiratasa(szotar, path):
    file = open(path, "w")
    for kulcs in szotar:
        file.write(str(kulcs[0]))
        file.write("\t")
        file.write(str(kulcs[1]))
        file.write("\t")
        file.write(szotar[kulcs])
        file.write("\n")
    file.close()


def szotar_betoltes(path: str):
    szotar = {}
    file = open(path, "r")
    for sor in file:
        adat = sor.strip().split()
        szotar[(int(adat[0]), int(adat[1]))] = adat[2]
    file.close()
    return szotar


def fafajta_lekerdezese(fak):
    x = egesz_szam_bekerese("x")
    y = egesz_szam_bekerese("y")
    hely = (x, y)
    if hely in fak:
        print("A fa fajtája:", fak[hely])
    else:
        print("Nincs fa az adott helyen.")


menu = ""
fak_szotar_path = "fak.csv"
fak = szotar_betoltes(fak_szotar_path)

while menu != "0":
    menu_opciok()
    menu = input()
    if menu == "1":
        uj_fa()
    elif menu == "2":
        fafajta_lekerdezese(fak)
szotar_kiiratasa(fak, fak_szotar_path)
