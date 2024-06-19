#Variables/ Proměnné

""" Proměnná je vytvořena v okamžiku, kdy jí poprvé přiřadíš hodnotu. """

x = 5
y = "Jonáš"
print(x)
print(y)


""" Proměnné nemusí být nutně deklarována s konkrétním typem a mohou dokonce měnit typ i poté, co byly nastaveny. """

x = 4       # <- nenapíše se protože proměnna ,,sally je pod ní""
x = "Sally" # <- toto se napíše neboť, program bere co je níže to je důvod proč se 4 nenapíše
print(x)


""" Pokud chcete zadat určitý datový typ proměnné, můžete to provést pomocí funkce casting. """

x = str(3)    # x bude'3'
y = int(3)    # y bude 3
z = float(3)  # z bude 3.0

""" Datový typ proměnné můžete určit pomocí funkce type(). """

x = 5
y = "Jonáš"
print(type(x))
print(type(y))


""" Jednoduché nebo dvojité uvozovky? """

x = "John"
# je totéž jako
x = 'John'

""" Rozlišování velkých a malých písmen """

a = 4
A = "Sally"
#A nepřepíše a


""" Názvy proměnných """


""" Proměnná může mít krátký název (jako x a y) nebo popisnější název (age, carname, total_volume). 

Pravidla pro proměnné v jazyce Python:

    •Název proměnné musí začínat písmenem nebo podtržítkem.
    •Název proměnné nesmí začínat číslem
    •Název proměnné může obsahovat pouze alfanumerické znaky a podtržítka (A-z, 0-9 a _ ).
    •V názvech proměnných se rozlišují velká a malá písmena (age, Age a AGE jsou tři různé proměnné).
    •Název proměnné nemůže obsahovat žádné z klíčových slov jazyka Python. (klíčová slova jsou myšlena jako funkce while print) """


myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


""" TOTO NEFUNGUJE! protože to obsahuje věci které tak nemůžou být 
2myvar = "John"
my-var = "John"
my var = "John" """





#Mnoho hodnot k více proměnným


""" Python umožňuje přiřadit hodnoty více proměnným na jednom řádku: """

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


""" Jedna hodnota pro více proměnných 
Na jednom řádku můžete přiřadit stejnou hodnotu více proměnným:
"""


x = y = z = "Orange"
print(x)
print(y)
print(z)



""" Rozbalení sbírky
Pokud máte kolekci hodnot v seznamu, tuplu atd. 
Python umožňuje extrahovat hodnoty do proměnných. Tomu se říká rozbalování.
 """

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)










#Výstupní proměnné


""" Funkce print() v jazyce Python se často používá k vypisování proměnných. """


x = "Python is awesome"
print(x)



""" Ve funkci print() se vypisuje více proměnných oddělených čárkou: """


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)



""" Můžete také použít operátor + k vypsání více proměnných: """

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)


""" U čísel funguje znak + jako matematický operátor: """

x = 5
y = 10
print(x + y)


""" V případě, že se ve funkci print() pokusíte zkombinovat řetězec a číslo pomocí operátoru +, zobrazí Python chybu: """


x = 5
y = "John"
#print(x + y) <- nebude fungovat!



""" Nejlepší způsob, jak ve funkci print() vypsat více proměnných, je oddělit je čárkami, které podporují i různé datové typy:"""



x = 5
y = "John"
print(x, y)




""" Globální proměnné """

""" Proměnné, které jsou vytvořeny mimo funkci (jako ve všech příkladech na předešlých řádcích), se nazývají globální proměnné.

Globální proměnné může používat každý, a to jak uvnitř funkcí, tak mimo ně. 


Vytvoření proměnné mimo funkci a její použití uvnitř funkce

"""

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()


""" 

Pokud uvnitř funkce vytvoříte proměnnou se stejným názvem, bude tato proměnná lokální a bude ji možné použít pouze uvnitř funkce. 
Globální proměnná se stejným názvem zůstane tak, jak byla, globální a s původní hodnotou.


Vytvoření proměnné uvnitř funkce se stejným názvem jako globální proměnná

 """



x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



""" Globální klíčové slovo

Pokud vytvoříte proměnnou uvnitř funkce, je tato proměnná lokální a lze ji použít pouze uvnitř dané funkce.

Chcete-li vytvořit globální proměnnou uvnitř funkce, můžete použít klíčové slovo global.

Pokud použijete klíčové slovo global, proměnná patří do globálního oboru:


 """



def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



""" 

Také pokud chcete změnit globální proměnnou uvnitř funkce, použijte klíčové slovo global.


Chcete-li změnit hodnotu global proměnné uvnitř funkce, odkažte se na tuto proměnnou pomocí klíčového slova global:


 """


x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)