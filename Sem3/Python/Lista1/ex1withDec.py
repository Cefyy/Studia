import decimal as d
zakupy = [d.Decimal(2.05),d.Decimal(1.45),d.Decimal(3.5)]

def vat_paragon(lista):
    suma=0
    for x in lista:
        suma = suma + x*d.Decimal(0.23)
    return suma


def vat_faktura(lista):
    suma=0
    for x in lista:
        suma = suma + x
    return suma*d.Decimal(0.23)

print(f"{vat_faktura(zakupy):.17f}")
print(f"{vat_paragon(zakupy):.17f}")
print(vat_faktura(zakupy)==vat_paragon(zakupy))