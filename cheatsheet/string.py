#Strings/ Řetězce







""" 

Řetězce v pythonu jsou obklopeny buď jednoduchými, nebo dvojitými uvozovkami.

'ahoj' je totéž co "ahoj".

Řetězcový literál můžete zobrazit pomocí funkce print(): 


"""

print("Hello")
print('Hello')

#Uvnitř uvozovek uvozovky

""" Uvnitř řetězce můžete použít uvozovky, pokud se neshodují s uvozovkami obklopujícími řetězec: """

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')


#Přiřazení řetězce k proměnné / Multiline Strings

""" Přiřazení řetězce k proměnné se provádí pomocí názvu proměnné, za kterým následuje znaménko rovnosti a řetězec: """

a = "Hello"
print(a)


#Víceřádkové řetězce

""" Víceřádkový řetězec můžete do proměnné přiřadit pomocí tří uvozovek: """


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#Nebo tři jednoduché uvozovky:

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)





#Řetězce jsou pole / Strings are Arrays

""" 
Stejně jako v mnoha jiných populárních programovacích jazycích jsou řetězce v Pythonu pole bajtů představující unicode znaky.

Python však nemá znakový datový typ, jednotlivý znak je prostě řetězec o délce 1.

Pro přístup k prvkům řetězce lze použít hranaté závorky.
"""



""" Získejte znak na pozici 1 (nezapomeňte, že první znak má pozici 0): """

a = "Hello, World!"
print(a[1])


#Smyčkování v řetězci / Looping Through a String

""" Protože řetězce jsou pole, můžeme znaky v řetězci procházet ve smyčce pomocí cyklu for. """


""" Ve smyčce projděte písmena ve slově "banana": """

for x in "banana":
  print(x)


# Délka řetězce / String Length


""" Chcete-li zjistit délku řetězce, použijte funkci len(). """

""" Funkce len() vrací délku řetězce: """

a = "Hello, World!"
print(len(a))



# Kontrolní řetězec / Check String



""" Chceme-li zjistit, zda se v řetězci vyskytuje určitý znak nebo fráze, můžeme použít klíčové slovo in. """

""" Zkontrolujte, zda se v následujícím textu vyskytuje slovo "free": """

txt = "The best things in life are free!"
print("free" in txt)




""" Použijte to v příkazu if: """

""" Vypsat pouze v případě, že je přítomen údaj "free": """

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


#Zkontrolujte, zda NE / Check if NOT


""" Chceme-li zjistit, zda se určitá fráze nebo znak v řetězci NEvyskytuje, můžeme použít klíčové slovo not in. """

""" Zkontrolovat, zda v následujícím textu NENÍ slovo " expensive ": """

txt = "The best things in life are free!"
print("expensive" not in txt)

""" Použijte to v příkazu if: """


txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")









# Krájení řetězců / Slicing Strings



""" 
Pomocí slice syntax můžete vrátit rozsah znaků.

Chcete-li vrátit část řetězce, zadejte počáteční a koncový index oddělený dvojtečkou.
 """

""" Získejte znaky od pozice 2 do pozice 5 (nejsou zahrnuty): """

b = "Hello, World!"
print(b[2:5])

# Řezání od začátku / Slice From the Start

""" Vynecháním počátečního indexu bude rozsah začínat prvním znakem: """

""" Získejte znaky od začátku do pozice 5 (není součástí): """

b = "Hello, World!"
print(b[:5])



# Řez až do konce / Slice To the End

""" Vynecháním koncového indexu se rozsah posune až na konec: """

""" Získejte znaky od pozice 2 až do konce: """

b = "Hello, World!"
print(b[2:])



#Negativní indexování / Negative Indexing

""" Používejte záporné indexy pro začátek řezu od konce řetězce:  """


""" 
Získejte znaky:

Od: "o" v "World!" (pozice -5)

Do, ale nezahrnuto: "d" v "World!" (pozice -2): 
"""

b = "Hello, World!"
print(b[-5:-2])




# Úprava řetězců / Modify Strings



#Upper Case

""" Metoda upper() vrací řetězec s velkými písmeny: """


a = "tento cely text bude velky"
print(a.upper())


#Lower Case

""" Metoda lower() vrací řetězec s malými písmeny: """

a = "TENTO CELY TEXT MALY!"
print(a.lower())


# Odstranění bílého místa / Remove Whitespace

""" 
Bílá místa jsou mezery před a/nebo za vlastním textem a velmi často je chcete odstranit. 

Metoda strip() odstraní bílé znaky na začátku nebo na konci:
"""

a = " Hello, World! "
print(a.strip()) # vrátí "Hello, World!" 

# Nahradit řetězec / Replace String

""" Metoda replace() nahradí řetězec jiným řetězcem: """

a = "Hello, World!"
print(a.replace("H", "J"))

# Rozdělení řetězce / Split String

""" 
Metoda split() vrací seznam, kde se text mezi zadaným oddělovačem stává položkami seznamu. 

Metoda split() rozdělí řetězec na podřetězce, pokud najde instance oddělovače:
"""

a = "Hello, World!"
print(a.split(",")) # vrátí ['Hello', ' World!'] 





# Spojování Řetězců / String Concatenation


""" Chcete-li spojit dva řetězce, můžete použít operátor +. """


""" Sloučení proměnné a s proměnnou b do proměnné c: """

a = "Hello"
b = "World"
c = a + b
print(c)

""" Chcete-li mezi ně přidat mezeru, přidejte znak " ": """

a = "Hello"
b = "World"
c = a + " " + b
print(c)






# Formát řetězce / String Format

""" Jak jsme se dozvěděli v kapitole o proměnných v Pythonu, nelze takto kombinovat řetězce a čísla: """

age = 36
#txt = "My name is John, I am " + age # <- nefunguje protože nemůžeme použít text + číslo
print(txt) 

""" Můžeme však kombinovat řetězce a čísla pomocí f-strings nebo metody format()! """

#F-Strings

"""  
Funkce F-String byla zavedena v jazyce Python 3.6 a nyní je preferovaným způsobem formátování řetězců.

Chcete-li zadat řetězec jako f-řetězec, jednoduše vložte před řetězcový literál znak f a přidejte kudrnaté závorky {} jako zástupné znaky pro proměnné a další operace.
"""

age = 36
txt = f"My name is John, I am {age}"
print(txt)








# Zástupné symboly a modifikátory / Placeholders and Modifiers

""" Zástupný symbol může obsahovat proměnné, operace, funkce a modifikátory pro formátování hodnoty. """

price = 59
txt = f"The price is {price} dollars"
print(txt)

""" Zástupný symbol může obsahovat modifikátor pro formátování hodnoty.

Modifikátor se uvede přidáním dvojtečky :, za kterou následuje legální typ formátování, například .2f, což znamená číslo s pevnou desetinnou čárkou a dvěma desetinnými místy: """

""" Zobrazení ceny se dvěma desetinnými místy: """

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

""" Zástupný symbol může obsahovat kód Pythonu, například matematické operace: """

""" Provede matematickou operaci v zástupném symbolu a vrátí výsledek: """

txt = f"The price is {20 * 59} dollars"
print(txt)







#Escape Character

""" Chcete-li do řetězce vložit nepovolené znaky, použijte znak escape.

Znak escape je zpětné lomítko \ následované znakem, který chcete vložit.

Příkladem nelegálního znaku je dvojitá uvozovka uvnitř řetězce, který je obklopen dvojitými uvozovkami: """




""" Pokud použijete dvojité uvozovky uvnitř řetězce, který je obklopen dvojitými uvozovkami, dojde k chybě:

txt = "We are the so-called "Vikings" from the north." """


""" Tento problém vyřešíte pomocí znaku escape \": """

txt = "We are the so-called \"Vikings\" from the north." 

""" Další znaky jsou když tak tady: https://www.w3schools.com/python/python_strings_escape.asp """
















# Řetězcové metody / String Methods 

""" Všechny metody: https://www.w3schools.com/python/python_strings_methods.asp """





#capitalize()

""" První písmeno v této větě se napíše s velkým počátečním písmenem: """

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)






#casefold()

""" Řetězec napiše malými písmeny: """

txt = "Hello, And Welcome To My World!"

x = txt.casefold()

print(x)







#center()

""" Napiše slovo "banana", které zabírá prostor 20 znaků, s "banana" uprostřed: """

txt = "banana"

x = txt.center(20)

print(x)






#count()

""" Vrátí počet výskytů hodnoty "apple" v řetězci: """

txt = "I love apples, apple are my favorite fruit"

x = txt.count("apple")

print(x)






#encode()

""" UTF-8 encode the string: """

txt = "My name is Ståle"

x = txt.encode()

print(x)







#endswith()

""" Zkontrolujte, zda řetězec končí interpunkčním znaménkem (.): """

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)








""" Zkontrolujte, zda pozice 5 až 11 končí výrazem "my world.": """

txt = "Hello, welcome to my world."

x = txt.endswith("my world.", 5, 11)

print(x)









#expandtabs()

""" Nastavte velikost tabulátoru na 2 bílá místa: """

txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)









#find()


""" Kde v textu je slovo "welcome"?: """

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)







#format()

""" Vložte cenu do náhradního pole, cena by měla být ve formátu s pevnou desetinnou čárkou a dvěma desetinnými místy: """

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)








#index()

""" Kde v textu je slovo "welcome"?: """

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)








#isalnum()

""" Zkontrolujte, zda jsou všechny znaky v textu alfanumerické: """

txt = "Company12"

x = txt.isalnum()

print(x)


if x == True:
 print ("Správně všechny znaky jsou alfanumerické")
else:
 print("špatně protože znaky nejsou alfanumerické")

""" 
Metoda isalnum() vrací hodnotu True, pokud jsou všechny znaky alfanumerické, tedy písmena abecedy (a-z) a čísla (0-9).

Příklad znaků, které nejsou alfanumerické: (mezera)!#%&? atd. 
"""









#isalpha()

""" Zkontrolujte, zda jsou všechny znaky v textu písmena: """

txt = "CompanyX"

x = txt.isalpha()

print(x)

if x == True:
 print ("Správně všechny znaky jsou písmena")
else:
 print("špatně protože všechny znaky nejsou v písmena")









#isascii()

""" Zkontrolujte, zda jsou všechny znaky v textu znaky ascii: """

txt = "Company123"

x = txt.isascii()

print(x)

if x == True:
 print ("Správně všechny znaky jsou ascii")
else:
 print("špatně protože znaky nejsou v ascii")









#isdecimal()

""" Zkontrolujte, zda jsou všechny znaky v řetězci desetinná čísla (0-9): """

txt = "1234"

x = txt.isdecimal()

print(x)

if x == True:
 print ("Správně všechny znaky jsou desetinná čísla")
else:
 print("špatně protože né všechny znaky jsou desetinná čísla")


a = "\u0030" #unicode pro 0
b = "\u0047" #unicode pro G

print(a.isdecimal())
print(b.isdecimal())










#isdigit()

""" Zkontrolujte, zda jsou všechny znaky v textu číslice: """

txt = "50800"

x = txt.isdigit()

print(x)


if x == True:
 print ("Správně všechny znaky jsou číslice")
else:
 print("špatně protože se zde nachází znaky které nejsou číslice")









#isidentifier()

""" Zkontroluje, zda je řetězec platným identifikátorem: """

txt = "Demo"

x = txt.isidentifier()

print(x)

""" 
Metoda isidentifier() vrací True, pokud je řetězec platným identifikátorem, jinak False.

Řetězec je považován za platný identifikátor, pokud obsahuje pouze alfanumerická písmena (a-z) a (0-9) nebo podtržítka (_). Platný identifikátor nesmí začínat číslem ani obsahovat mezery. 
"""








#islower()

""" Zkontrolujte, zda jsou všechny znaky v textu psány malými písmeny: """

txt = "hello world!"

x = txt.islower()

print(x)


if x == True:
 print ("Správně všechny znaky jsou napsany malým písmenem")
else:
 print("špatně protože není všechno napsáno malým písmenem")







#isnumeric()

""" Zkontrolujte, zda jsou všechny znaky v textu číselné: neuznává čísla jako -1, 1.5"""

txt = "565543"

x = txt.isnumeric()

print(x)

if x == True:
 print ("Správně všechny znaky jsou číselné")
else:
 print("špatně nejsou číselné znaky")








#isprintable()

""" Zkontrolujte, zda jsou všechny znaky v textu tisknutelné: """

txt = "Hello! Are you #1?"

x = txt.isprintable()

print(x)

if x == True:
 print ("Správně všechny znaky v textu jsou tisknutelné")
else:
 print("špatně nachází se zde některé znaky které se nedají tisknout")









#isspace()

""" Zkontrolujte, zda jsou všechny písmena v textu mají bílou mezeru: """

txt = "   "

x = txt.isspace()

print(x)


if x == True:
 print ("Správně protožeo obsahuje bílou mezeru")
else:
 print("špatně protože neobsahuje bílou mezeru")



txt = "   s   " # <- False protože je tam to S

x = txt.isspace()

print(x)









#istitle()

""" Zkontrolujte, zda každé slovo začíná velkým písmenem: """

txt = "Hello, And Welcome To My World!"

x = txt.istitle()

print(x)


if x == True:
 print ("Správně všechny znaky začínájí velkým písmenem")
else:
 print("špatně protože všechny znaky nezačínají velkým písmenem")








#isupper()

""" Zkontrolujte, zda jsou všechny znaky v textu napsány velkými písmeny: """

txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

if x == True:
 print ("Správně všechny znaky jsou napsány velkými písmeny")
else:
 print("špatně protože znaky nejsou napsány velkými písmeny")









#join()

""" Spojí všechny položky v tuple do řetězce pomocí znaku hash jako oddělovače: """

myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)





myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)










#ljust()

""" Vrátí 20 znaků dlouhou, vlevo zarovnanou verzi slova "banana": když tam dám rjust tak to posune od prava"""

txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")




""" Použití písmene "O" jako výplňového znaku: """

txt = "banana"

x = txt.ljust(20, "O")

print(x)








#lower()

""" Řetězec napíše malými písmeny: """

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)








#lstrip()

""" Odstranění mezer vlevo od řetězce: """

txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")


""" Odstraňte úvodní znaky: """

txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)







#maketrans()

""" Vytvořte mapovací tabulku a pomocí ní v metodě translate() nahraďte všechny znaky "S" znakem "P": """

txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

""" Samotná metoda maketrans() vrací slovník popisující každou náhradu v unicode: """

txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
print(str.maketrans(x, y, z))









#partition()

""" 
Vyhledá slovo "bananas" a vrátí tuple se třemi prvky:

1 - vše před "match"
2 - "match"
3 - vše, co následuje po "match" 
"""

txt = "I could eat bananas all day"

x = txt.partition("bananas")

print(x)



txt = "I could eat bananas all day"

x = txt.partition("apples")

print(x)






#replace()

""" Nahraď slovo "bananas": """

txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)






#rfind()

""" Kde v textu se naposledy vyskytuje řetězec "casa"?: """

txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)






#rindex()

""" Kde v textu se naposledy vyskytuje řetězec "casa"?: """

txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)






#rjust()

""" Vrátí 20 znaků dlouhou, vpravo zarovnanou verzi slova "banana": """

txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")








#rpartition()

""" 
Vyhledá poslední výskyt slova "bananas" a vrátí tuple se třemi prvky:

1 - vše před "match"
2 - "match"
3 - vše za "match"
"""


txt = "I could eat bananas all day, bananas are my favorite fruit"

x = txt.rpartition("bananas")

print(x)







#rsplit()

""" Rozdělení řetězce na seznam pomocí čárky, za kterou následuje mezera (, ) jako oddělovač: """

txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)







#rstrip()

""" Odstranění bílých mezer na konci řetězce: """

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")










#split()

""" Rozdělení řetězce na seznam, kde každé slovo je položkou seznamu: """

txt = "welcome to the jungle"

x = txt.split()

print(x)











#splitlines()

""" Rozdělí řetězec na seznam, kde každý řádek je položka seznamu: """

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)




""" Řetězec rozdělíte, ale zachováte zalomení řádků: """

txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines(True)

print(x)












#startswith()

""" Zkontroluje, zda řetězec začíná slovem "Hello": """

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)


if x == True:
 print ("Správně protože string začíná slovem Hello")
else:
 print("špatně protože string nezačíná slovem Hello")











#strip()

""" Odstranění mezer na začátku a na konci řetězce: """

txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")










#swapcase()

""" Malá písmena napiše velkými písmeny a velká písmena malými: """

txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)








#title()

""" První písmeno v každém slově napiše velkým písmem: """

txt = "Welcome to my world"

x = txt.title()

print(x)






#translate() 

""" Nahradí všechny znaky "S" znakem "P": """

#pomocí slovníku s ascii kódy nahradit 83 (S) za 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))





#upper()

""" Psaní velkých písmen v řetězci: """

txt = "Hello my friends"

x = txt.upper()

print(x)







#zfill()

""" Vyplňuje řetězec nulami, dokud nebude mít 10 znaků: """

txt = "50"

x = txt.zfill(10)

print(x)