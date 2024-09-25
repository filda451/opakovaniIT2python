#1. Vytvořte proměnnou, do které vložíte své jméno.
promenna1 = "Filip"
#2. Vytvořte proměnnou, do které vložíte své příjmení.
promenna2 = "Osmancik"
#3. Vypište tyto dvě proměnné do konzole.
print(promenna1, promenna2)
#4. Vytvořte vstup pro uživatele, který bude moct zadat pouze věk (nikoli své jméno nebo jinou stringovou hodnotu).
vek = int(input("Napiš věk:" ))

if vek < 15:
    print("Jste dítě")
elif vek >= 18:
    print("Jste dospělý")
else:
    print("Neplatný věk")
#5. Vypište v konzoli délku první proměnné a druhé proměnné.
print(len(promenna1), len(promenna2))
#6. Vytvořte proměnnou, do které uložíte hodnotu 6.
promenna = 6
#7. Vytvořte cyklus, který bude mít 5 opakování a při každém opakování se přičte hodnota 3.
soucet = 0
for i in range(5):
    soucet += 3
print(soucet)
#8. Vypište v konzoli výslednou hodnotu po 5 cyklech.
print("Konecna hodnota po 5 cyklech je:", soucet)
#9. Vytvořte podmínku pro uživatele, který zadá věk - 1. Pokud zadá jen celočíselnou hodnotu program odpoví "Děkuji". 2. Pokud zadá jakoukoli jinou hodnotu program odpoví "Zadej jen celočíselnou hodnotu."
vek = input("Napiš věk:")

if vek.isdigit():
    print("Děkuji")
else:
    print("Musíš zadat celočíselnou hodnotu")
#10. Vytvořte proměnnou, do které uloží program náhodnou hodnotu od 1-10 a vypište ji do konzole. 
import random

# random hodnota od (1 do 10()
random_hodnota = random.randint(1, 10)

# Výsledek random hodnoty
print("random hodnota je:", random_hodnota)
#BONUS - Vytvořte z bodu 4. a 9. cyklus - pokud uživatel zadá špatnou hodnotu vrátí ho program zpět, aby zadal svůj věk.