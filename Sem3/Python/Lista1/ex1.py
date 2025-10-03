
zakupy = [2.05,1.45,3.5]

def vat_paragon(lista):
    suma=0
    for x in lista:
        suma = suma + x*0.23
    return suma


def vat_faktura(lista):
    suma=0
    for x in lista:
        suma = suma + x
    return suma*0.23

print(f"{vat_faktura(zakupy):.17f}")
print(f"{vat_paragon(zakupy):.17f}")
print(vat_faktura(zakupy)==vat_paragon(zakupy))