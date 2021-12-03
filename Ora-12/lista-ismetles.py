def feladat(szam):
    print("\n" + str(szam) + ". feladat")


print("Lista ismétlés")


def elso():
    feladat(1)
    lista = [7, 43, 132, 654, 432, 123, 3, 11, -1]

    def sort_list(lista):
        kell = True
        while kell:
            elozo = lista[0]
            kell = False
            for elem in lista:
                if elozo > elem:
                    kell = True
                elozo = elem
            for i in range(len(lista)):
                if i < (len(lista) - 1):
                    if lista[i] > lista[i + 1]:
                        temp = lista[i]
                        lista[i] = lista[i + 1]
                        lista[i + 1] = temp
            print(lista)
        return lista

    def jobb_sort(lista: list[int]) -> list[int]:
        rendezett_lista = lista.copy()
        for i in range(1, len(lista)):
            for j in range(len(lista) - i):
                if rendezett_lista[j] > rendezett_lista[j + 1]:
                    seged = rendezett_lista[j]
                    rendezett_lista[j] = rendezett_lista[j + 1]
                    rendezett_lista[j + 1] = seged
        return rendezett_lista

    sort_list(lista)

    # print()
    # print(jobb_sort(lista))

    def minimum_kereses(lista: list[int], hanyadik=0) -> int:
        return sort_list(lista)[hanyadik]

    print(minimum_kereses([4, 6, 7, 2, 3, 5, 8, 32, 2], 0))

    def osszeg(lista: list[int]) -> int:
        osszeg = 0
        for elem in lista:
            osszeg += elem
        return osszeg



elso()
