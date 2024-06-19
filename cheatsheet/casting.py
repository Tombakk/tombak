#Python Casting

#Zadávání typu proměnné


""" 

Můžete se setkat s případy, kdy budete chtít u proměnné zadat typ. To lze provést pomocí funkce casting. 
Python je objektově orientovaný jazyk a jako takový používá k definici datových typů třídy, včetně primitivních typů.

Casting v pythonu se proto provádí pomocí konstrukčních funkcí:

      • int() - zkonstruuje celé číslo z integer literálu, float literálu (odstraněním všech desetinných míst) nebo řetězcového literálu (pokud řetězec představuje celé číslo).
      • float() - zkonstruuje číslo float z integer literálu, float literálu nebo řetězcového literálu (pokud řetězec reprezentuje float nebo celé číslo).
      • str() - zkonstruuje řetězec z různých datových typů, včetně řetězců, integer literálů a floatových literálů.
 """

#Integers:

x = int(1)   # x bude 1
y = int(2.8) # y bude 2
z = int("3") # z bude 3

#float 

x = float(1)     # x bude 1.0
y = float(2.8)   # y bude 2.8
z = float("3")   # z bude 3.0
w = float("4.2") # w bude 4.2

#strings/ řetězce

x = str("s1") # x bude 's1'
y = str(2)    # y bude '2'
z = str(3.0)  # z bude '3.0'