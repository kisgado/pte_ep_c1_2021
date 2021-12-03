class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def egyenleg(self):
        print("A számla egyenlege:", self.balance)

    def osszeg(self):
        try:
            szam = int(input("Adja meg az összeget: "))
            if szam <= 0:
                raise ValueError
            if szam >= self.balance:
                raise ValueError
            return szam
        except ValueError:
            print("Hibás összeg.")

    def osszeg2(self):
        try:
            szam = int(input("Adja meg az összeget: "))
            if szam <= 0:
                raise ValueError
            return szam
        except ValueError:
            print("Hibás összeg.")

    def withdrawl(self):
        print("Mekkora összeget szeretne kivenni?")
        szam = self.osszeg()
        self.balance = self.balance - szam
        print("Sikeres pénzfelvétel.")
        self.egyenleg()

    def deposit(self):
        print("Mekkora összeget szeretne betenni?")
        szam = self.osszeg2()
        self.balance = self.balance + szam
        print("Sikeres letét.")
        self.egyenleg()


a = BankAccount("Asd", 1, 1312)
a.egyenleg()
a.withdrawl()
a.deposit()