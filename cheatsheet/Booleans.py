#Booleans

""" 
Booleans představují jednu ze dvou hodnot: True nebo False.

Při programování často potřebujete vědět, zda je výraz True nebo False.

V Pythonu můžete vyhodnotit libovolný výraz a získat jednu ze dvou odpovědí: True nebo False.

Při porovnávání dvou hodnot se výraz vyhodnotí a Python vrátí Boolean odpověď:
"""




print(10 > 9)
print(10 == 9)
print(10 < 9)

""" Při spuštění příkazu if vrátí Python hodnotu True nebo False: """

""" Vypíše zprávu podle toho, zda je podmínka True nebo False: """

a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


# Vyhodnocení hodnot a proměnných / Evaluate Values and Variables

""" Funkce bool() umožňuje vyhodnotit libovolnou hodnotu a vrátit vám True nebo False, """

print(bool("Hello"))
print(bool(15))

# Most Values are True / Většina hodnot je pravdivá

""" Téměř každá hodnota je vyhodnocena jako True, pokud má nějaký obsah.

Jakýkoli řetězec je True, kromě prázdných řetězců.

Jakékoli číslo je True, kromě 0.

Jakýkoli seznam, tuple, set a slovník jsou True, kromě prázdných. """


""" Následující vyhodnotí TRUE """

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])


# Některé hodnoty jsou nepravdivé / Some Values are False

""" Ve skutečnosti neexistuje mnoho hodnot, které se vyhodnotí jako False, kromě prázdných hodnot, jako jsou (), [], {}, "", číslo 0 a hodnota None. 
A samozřejmě hodnota False se vyhodnotí jako False. """

""" Následující příkaz vrátí hodnotu False: """

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


""" Ještě jedna hodnota, nebo v tomto případě objekt, se vyhodnotí jako False, a to v případě, že máte objekt vytvořený ze třídy s funkcí __len__, která vrací 0 nebo False: """

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


# Funkce mohou vracet Boolean / Functions can Return a Boolean

""" Můžete vytvářet funkce, které vracejí Boolean hodnotu: """

def myFunction() :
  return True

print(myFunction())

""" Na základě Boolean odpovědi funkce můžete spustit kód: """

""" Pokud funkce vrátí hodnotu True, vypište "YES!", jinak vypište "NO!": """

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


""" Python má také mnoho vestavěných funkcí, které vracejí boolean hodnotu, například funkci isinstance(), kterou lze použít k určení, zda je objekt určitého datového typu: """

""" Zjistí, zda je objekt integer, nebo ne: """

x = 200
print(isinstance(x, int))
