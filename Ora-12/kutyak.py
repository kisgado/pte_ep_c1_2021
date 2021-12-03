class Kutya:
    """
    Kutyák osztálya
    """

    def __init__(self, nev: str, kor: int, fajta: str):
        self.nev = nev
        self.kor = kor
        self.fajta = fajta

    def __str__(self):
        return self.nev + " egy " + str(self.kor) + " éves kutya, aki " + self.fajta + " fajtájú."


k = Kutya("Bodri", 10, "kuvasz")
k2 = Kutya("Buksi", 3, "puli")
print(k)
print(k2)
