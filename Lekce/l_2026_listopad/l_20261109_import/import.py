import math

print(f"Číslo PI je: {math.pi}")
print(f"Sinus 90 stupnu je: {math.sin(math.pi/2)}")

def bezpecne_deleni(a, b):
    try:
        vysledek = a / b
    except ZeroDivisionError as zde:
        print(f"Chyba: {zde}")
        return None
    except Exception as e:
        zprava = f"nelze dělit objekt {a} / {b}: {e}"
        raise Exception(zprava)
    finally:
        print("Dělení bylo dokončeno.")
        print("tento blok se provede vždy")
    return vysledek

print(bezpecne_deleni(10,2 ))
print(bezpecne_deleni(10,0 ))