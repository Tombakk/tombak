# Autor Tomáš Musil Skibidi
import math
výpočet = True
pi = math.pi

print("Vítej v této skibidi gyat kalkulačce")
while výpočet:
    x = input("Jaké je tvoje první číslo?")

    if not x.isdigit():
        print(f"{x} <- nejedná se o číslo")
    else:
        výpočet = False
        
y = input("+" "-" "/" "*")
z = input("Jaké je tvoje druhé číslo?")