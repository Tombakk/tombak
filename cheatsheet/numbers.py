#Čísla v Pythonu



""" V Pythonu existují tři číselné typy: """

int
float
complex

""" Proměnné numerických typů se vytvářejí, když jim přiřadíte hodnotu: """



x = 1    # int
y = 2.8  # float
z = 1j   # complex


""" Chcete-li ověřit typ libovolného objektu v Pythonu, použijte funkci type(): """

print(type(x))
print(type(y))
print(type(z))



#INT 
""" Int nebo integer je celé číslo, kladné nebo záporné, bez desetinných míst, neomezené délky. """

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

#Float

""" Float neboli "číslo s pohyblivou řádovou čárkou" je kladné nebo záporné číslo obsahující jedno nebo více desetinných míst. """

x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))


""" Float mohou být také vědecká čísla s písmenem "e", které označuje mocninu 10. """

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))


#Complex

""" Complex čísla se zapisují s "j" jako imaginární částí: """

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#Typ konverze

""" Můžete konvertovat z jednoho typu na jiný pomocí metod int(), float() a complex(): """

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#konvertovat z int na float:
a = float(x)

#Konvertovat z float na int:
b = int(y)

#Konvertovat z int na complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))



#Náhodné číslo

""" Python nemá funkci random() pro vytvoření náhodného čísla, ale má vestavěný modul s názvem random, který lze použít k vytváření náhodných čísel: """

import random

print(random.randrange(1, 10))