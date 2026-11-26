
#Tento řadek se mě zeptá: Kolik litrů benzínu chci natankovat.
Litry = float(input("Kolik litrů benzínu chcete natankovat? "))


#Tady se mě zeptá kolik stojí litr benzínu
cena = float(input("Zadejte cenu za litr benzínu: "))


#Tady mi spočíta kolik budu celkem za benzín platit
celkem = round(Litry * cena, 2)


#Jen řádek navíc
print()


#Vytiskne mi výslednou cenu za natankovaný benzín
print(f"Celkem budete platit ${celkem:.2f}")
