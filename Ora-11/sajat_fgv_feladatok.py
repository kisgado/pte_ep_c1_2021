import datetime
import time


def feladat(n):
    print("\n%d. feladat" % n)


def elso_feladat():
    def nev_beker():
        nev = input("Adja meg a nevét: ")
        return nev

    def nev_kiir(nev) -> None:
        print("Szia %s!" % nev)

    feladat(1)
    nev_kiir(nev_beker())


def masodik_feladat():
    def aktualis_ido():
        print("Az aktuális idő: %s " % datetime.datetime.now())

    feladat(2)
    aktualis_ido()


def harmadik_feladat():
    def varakozas(sec: int):
        print("Az aktuális idő: %s " % datetime.datetime.now())
        time.sleep(sec)
        print("Vártam %d másodpercet." % sec)
        print("Az aktuális idő: %s " % datetime.datetime.now())

    varakozas(int(input("Eddig várjak: ")))


def negyedik_feladat():
    feladat(4)
    netto = int(input("Nettó ár: "))
    print("Bruttó ár: %.2fft" % (netto * 1.27))


def otodik_feladat():
    feladat(5)

    def adat_beker() -> list:
        print("Adjon meg számokat -40 és 40 C fok között. Ha befejezte, adjon meg ezen kívüli értéket.")
        szamok = []
        szam = int(input("Adjon meg egy számot: "))
        while -40 <= szam <= 40:
            szamok.append(szam)
            szam = int(input("Adjon meg egy számot: "))
        return szamok

    def atlag_szamit(szamok: list) -> float:
        osszeg = 0
        db = 0
        for szam in szamok:
            osszeg += szam
            db += 1
        print(osszeg / db)
        return osszeg / db

    def magas_atlag_szamit(atlag: float, szamok: list) -> float:
        osszeg = 0
        db = 0
        for szam in szamok:
            if szam > atlag:
                osszeg += szam
                db += 1
        print(osszeg / db)
        return osszeg / db
    # nincs kész
    szamok = adat_beker()
    atlag = atlag_szamit(szamok)


# elso_feladat()
# masodik_feladat()
# harmadik_feladat()
# negyedik_feladat()
otodik_feladat()
