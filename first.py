# Definice funkce s podmínkou if
def sudy_nebo_lichy(cislo):
    if cislo % 2 == 0:
        SudeLiche = "sudé"
    else:
        SudeLiche = "liché"
    return f"Číslo {cislo} je {SudeLiche}."

# Volání funkce a ukládání návratových hodnot do proměnných
veta1 = sudy_nebo_lichy(5)
veta2 = sudy_nebo_lichy(1000000)

# Výstup pomocí print()
print(veta1)
print(veta2)