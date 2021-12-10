from math import pi
from random import *

from easygui import *


def feladat(n):
    print("%d. feladat" % n)


def first():
    feladat(1)
    x = float(enterbox("Adja meg a kör átmérőjét: "))
    print(x)
    if x < 0:
        msgbox("Hiba: negatív számot adott meg.")
    else:
        ker = 2 * (x / 2) * pi
        ter = ((x / 2) ** 2) * pi
        kiir = "A kör kerülete " + str(ker) + "\nA kör területe " + str(ter)
        msgbox(kiir)


def second():
    feladat(2)
    try:
        evszam = int(enterbox("Adjon meg egy évszámot."))
        if evszam % 4 == 0 and evszam % 100 != 0:
            ki = "A megadott év szökőév, mert osztható néggyel, de nem osztható százzal."
        elif evszam % 400 == 0:
            ki = "A megadott év szökőév, mert osztható négyszázzal."
        else:
            ki = "A megadott év nem szökőév, mert nem igaz egyik sem az albbiak közül:"
            ki = ki + "\n\tosztható néggyel, de nem osztható százzal"
            ki = ki + "\n\tosztható négyszázzal"
        msgbox(ki)
    except ValueError:
        msgbox("Hibás bemenet.")


def third():
    feladat(3)
    minimum = 1
    maximum = 99
    szam = randint(minimum, maximum)
    proba = 6
    szoveg = "Gondoltam egy számra " + str(minimum) + " és " + str(maximum) + " között, "
    szoveg = szoveg + str(proba) + " próbálkozásod van kitalálni."
    x = msgbox(szoveg, "Tippelő játék", "Induljon a játék!")
    nyert = False
    if x == "Induljon a játék!":
        print("asd")
        while proba > 0:
            szoveg = "Még " + str(proba) + " lehetőséged van."
            proba = proba - 1
            inp = enterbox(szoveg, title="Tippelő")
            if inp == "":
                msgbox("Nem adott meg értéket.", "Hiba")
            elif szam < int(inp):
                msgbox("Kisebb számra gondoltam.", "Tippelő", "Új tipp")
            elif szam > int(inp):
                msgbox("Nagyobb számra gondoltam.", "Tippelő", "Új tipp")
            elif szam == int(inp):
                proba = 0
                nyert = True
                ki = "Gratulálok, eltaláltad!"
                msgbox(ki, "Tippelő", "Nyertem!")
        if not nyert:
            ki = "Sajnos nem nyertél.\nErre a számra gondoltam: " + str(szam)
            msgbox(ki, "Tippelő", "Vesztettem.")


"""
first()
second()
"""
third()
