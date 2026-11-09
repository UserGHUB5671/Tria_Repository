def scitani(a, b):
    return a + b
soucet = scitani(5, 3)
print("Součet je:", soucet)
soucet2 = scitani(10, 15)
print("Součet je:", soucet2)

def deleni(a, b):
    if b == 0:
        return "Chyba: Dělení nulou není povoleno."
    else:
        return a / b
print("Dělení je:", deleni(10, 2))