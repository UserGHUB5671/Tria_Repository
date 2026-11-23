
print("Python", "je", "skvělý")               # Vypíše: Python je skvělý
print("2026", "11", "12", sep="-")            # Vypíše: 2026-11-12
print("Načítám data", end="... ")
print("Hotovo!")                              # Vypíše na stejný řádek: Načítám data... Hotovo!
print()                                       # Prázdný print() pouze odřádkuje



leva_kapsa = "klíče"
prava_kapsa = "mobil"

print("-------------")
 
# Elegantní pythonovské prohození hodnot
leva_kapsa, prava_kapsa = prava_kapsa, leva_kapsa

print(leva_kapsa)   # mobil
print(prava_kapsa)  # klíče