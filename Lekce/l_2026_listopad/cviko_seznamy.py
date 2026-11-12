import math

jmeno = "Petr"
vek = 30
print(f"Jmenuji se {jmeno} a je mi {vek} let.")

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
numbers.sort()
print(f"seřazeny seznam: {numbers}")
print(f"první prvek sezanmu: {numbers[0]}")
print(f"poslední prvek seznamu: {numbers[-1]}")


student = {
    "jmeno": "Petr",
    "vek": 20,
    "predmety": ["Matematika", "Fyzika", "Chemie"]
}
print(f"Student: {student}");


data = [3, 3, 3, 4, 5, 5, 6, 7, 8, 9,]
unique_data = set(data)
print(f"Unikátní hodnoty: {unique_data}")



for i  in range(1,11):
    if i % 3 == 0:
        print("je delitelne 3")
    elif i % 5 == 0:
        print("je delitelne 5")
    else:
        print(i)



def vypocet_obvodu_obdelniku(delka, sirka):
    return 2 * (delka + sirka)

print(f"Obvod obdelniku je: {vypocet_obvodu_obdelniku(5, 3)}")

odmocnina = math.sqrt(16)
print(f"Odmocnina z 16 je: {odmocnina}")