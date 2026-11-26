Litry = float(input("Kolik litrů benzínu chcete natankovat? "))
cena = float(input("Zadejte cenu za litr benzínu: "))

celkem = round(Litry * cena, 2)

print()
print(f"Celkem budete platit ${celkem:.2f}")
