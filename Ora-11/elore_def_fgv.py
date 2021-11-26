print(chr(80), chr(121), chr(116), chr(104), chr(111), chr(110), sep='')
print(ord("P"))
print(ord("a"))
print(ord("A"))
print(ord(chr(80)))
print(float("3.5"))
print(type(float("3.5")))
print(int("12", base=16))
print(hex(18))
print(bin(18))
print(oct(18))
num = 42.73485
print(num)
print(int(num))         # nem kerekít, csak levágja
print(round(num))       # int
print(round(num, 0))    # egész pontosságú, de float
print(round(num, 2))    # float

try:
    print(a)
except NameError:
    print("Nem definiált változó.")
try:
    chr(num)
except TypeError:
    print("Nem megfelelő típusú változó.")
try:
    chr(9999999999999999)
except OverflowError:
    print("Túl nagy érték a változóban.")
try:
    chr(9999999)
except ValueError:
    print("A változó értéke nincs a megfelelő határok között.")
# print("a) : SyntaxError
a, b = 2, 4
if a == 4 or b != 4:
    print("nyert")
if a == 4 or b == 4:
    print("majdnem nyert")
