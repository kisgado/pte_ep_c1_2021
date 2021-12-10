from easygui import *

response = msgbox("Felirat", "Cím", "Gomb", "asd.png")
print(response)

color = buttonbox("Melyik színt választja?", title="Színek", choices=["Piros", "Kék", "Zöld"], images="asd.png",
                  default_choice="Kék")
print(color)

flavor = enterbox("Melyik a kedvenc fagylaltod?", title="Fagylaltok", default="Vanília", image="asd.png")
if flavor is not None:
    valasz = "A választott íz: " + flavor
    msgbox(valasz)
