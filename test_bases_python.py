"zre gfseg srt hdr h"
# commentaire en début de page devient la doc de la page

a = 25

def add(a, b):
    # commentaire en début de fonction devient la doc de la fonction
    "Returns the sum of a and b"
    res = a
    res += b
    return res

print(a)

if __name__ == "__main__":
    print(add(2, 2))
    
    
# ------------------- FREECODECAMP - PYTHON ------------------------------- #    
print('FREECODECAMP - TRAINING PYTHON')
print('---------------------------------')

# BIGGEST LETTER
print('BIGGEST LETTER')
big = max('Hello world')
print(big, 'is the biggest caracter')                  
# w car w est la lettre "max" de ce texte
print('---------------------------------')

# TINIEST LETTER
print('TINIEST LETTER')
tiny = min('Hello world')
print(tiny, "(space is the tiniest caracter)")
# affiche un espace car espace  = minimum dans l'ordre alphabétique
print('---------------------------------')

# LOOP
print('LOOP')
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
print('---------------------------------')    
     
# SMALLEST NUMBER 
print('SMALLEST NUMBER')
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
    print("Loop :", itervar, "; smallest =", smallest)
print("After : the smallest number is :", smallest)
# Before: None
# and Smallest: 3
print('---------------------------------')

# LARGEST NUMBER
print('LARGEST NUMBER')
largest = -1
print('Before', largest)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest :
        largest = the_num
    print('Largest number :', largest, '; Current number :', the_num)
print('After : the largest number is', largest)
print('---------------------------------')

# COUNTER
print('COUNTER')
counter = 0
print('Before : counter = ', counter)
for thing in [10, 11, 12, 13, 14, 15]:
    counter += 1
    print(counter,'-', thing)
print('After : counter =', counter)
print('---------------------------------')

# SUM & AVERAGE
print('SUM & AVERAGE')
count = 0
finalsum = 0
print('Before : count =', count, '; sum =',finalsum)
for value in [1, 2, 3, 4, 5]:
    count += 1
    finalsum += value
    print(count, finalsum, value)
# sum / count = average
print('After : count =', count, '; sum =', finalsum, '; average =', finalsum / count)
print('---------------------------------')

# BOOLEAN
print("BOOLEAN")
found = False
print("Before : found = ", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print("After : found = ", found)
# found = True après le 3 car pas de condition pour le faire devenir False

print()
print("0 == 0 =>", 0 == 0)           # True
print("0 is 0.0 =>", 0 is 0.0)         # False
print("0 is not 0.0 =>", 0 is not 0.0)     # True
# print("0 = 0.0 =>", 0 = 0.0) impossible => erreur de syntaxe
print('---------------------------------')

# LOOP IN STRING
print("LOOP IN STRING")
print("/!\ for n in banana, print(n) donne :")
for n in "banana":
    print(n)
# b a n a n a car n = iteration variable, pas lettre
fruit = "banana"
secondLetter = fruit[1]
print("The second letter in banana is :", secondLetter)
# a

x = 1
y = fruit[x-1]
print("The first letter in banana is :", y)
# b
print("Longueur du mot banana : len(fruit) =", len(fruit))

index = 0
while index < len(fruit):
    letter = fruit[index]
    print("index = ", index, "; letter = ", letter)
    index += 1
print('---------------------------------')

# SLICING STRINGS
print("SLICING STRINGS")
str = "Monty Python"
print(str[6:20])
# Python
print(str[:])
# Monty Python
print('---------------------------------')

# SPACE IN STRING
print("SPACE IN STRING")
a = "Hello"
b = a + "There"
print(b)
# HelloThere
c = a + " " + "There"
print(c)
# Hello There
print('---------------------------------')

# FIND IN STRING
print("FIND IN STRING")
fruit = "apple"
print("'n' in the word fruit ?", 'n' in fruit)
# False
print("'nan' in the word fruit ?", 'nan' in fruit)
# True
if 'a' in fruit:
    print("Found an 'a'!")
# Found an 'a'!
print('---------------------------------')

# COMPARE STRINGS
print("COMPARE STRINGS")
word = "apple"
if word == "banana":
    print("All right, banana.")
if word < "banana":
    print("Your word " + word.upper() + " come before banana")
elif word > "banana":
    print("Your word " + word.upper() + " come after banana")
else:
    print("All right, your word is banana.")
print('---------------------------------')

# TYPE
print("TYPE")
stuff = "Hello world"
print("stuff est de type : ", type(stuff))
print("dir(stuff) affiche les méthodes possibles pour un String :")
print(dir(stuff))
print('---------------------------------')

# SEARCHING A STRING
print("SEARCHING A STRING")
fruit = "banana"
position = fruit.find("na")
print("Position de 'na' dans banana : ", position)
# index 2
pos = fruit.find("z")
print("Position de 'z' dans banana : ", pos)
# index -1 car non trouvé
print('---------------------------------')

# SEARCH & REPLACE
print("SEARCH & REPLACE")
greet = "Hello Bob"
print("Variable 'greet' = ", greet)
replaceString = greet.replace("Bob", "Sandra")
print("Hello Bob remplacé par : ", replaceString)
# Hello Sandra
replaceString = greet.replace("o", "X")
print("o remplacé par X : ", replaceString)
# HellX BXb
print('---------------------------------')

# WHITESPACE
print("WHITESPACE")
greet = "   Hello Bob   "
print("greet.lstrip() : " + "'" + greet.lstrip() + "'")
# RigthStrip = retrait espace devant : 'Hello Bob   '
print("greet.rstrip() : " + "'" + greet.rstrip() + "'")
# LeftStrip = retrait espace derrière : '   Hello Bob'
print("greet.strip() : " + "'" + greet.strip() + "'")
# retrait espace devant et derrière : 'Hello Bob'
print('---------------------------------')

# START/END WITH
print("START/END WITH")
greet = "Hello Bob"
print("greet.startswith('Hello')?", greet.startswith("Hello"))
# True
print("greet.endswith('Bob')?", greet.endswith("Bob"))
# True
print('---------------------------------')

# COMBINE TO PARSE & EXTRACT
print("COMBINE TO PARSE & EXTRACT")
data = "From john.doe@uct.ac.za Mon Oct 9 11:36:16 2023"
atposition = data.find("@")
print("Index du @ :", atposition)
# 13
spposition = data.find(" ", atposition)
print("Index du 1er espace après le @ :", spposition)
# 23
host = data[atposition+1: spposition]
print("String entre @ et le 1er espace aprs le @ :",host)
# uct.ac.za
print('---------------------------------')

# READING FILES = A HANDLE
print()
print("READING FILES")
print("To open a files : handle = open('filename', 'mode')")
print("mode = 'r' for read or 'w' for write")
# un "file handle" (gestionnaire de fichier) = référence à un fichier ouvert par un programme
try:
    fhand = open('readtest.txt')
except:
    print("File cannot be opened")
    quit()
print("Type de fichier : ", fhand)
# <_io.TextIOWrapper name='readtest.txt' mode='r' encoding='cp1252'>
content = fhand.read()
print("Dans readtest.txt, il est écrit :")
print(content)
# readTest ne contient que ces lignes

# Revenir au début du fichier car curseur à la fin puisqu'on vient de le lire
fhand.seek(0)
count = 0
for line in fhand:
    count += 1
print("Nombre de lignes dans ce fichier :", count)
# 1

# fhand.seek(0) ou 
fhand = open('readtest.txt')
nbcaracters = fhand.read()
print("Nombre de caractères dans ce fichier :", len(nbcaracters))
# 35
print('---------------------------------')

# NEWLINE CHARACTER
print()
print("NEWLINE CHARACTER")
stuff = "Hello\nWorld"
print("'\\n' pour passer à la ligne :")
print(stuff)
print('---------------------------------')

# LISTS = MUTABLES
print("LISTS (MUTABLES)")
fruits = ["apple", "banana", [10, 20]]
x = fruit[1]
print(x)
# banana
print("fruit[2][1] = ", fruits[2][1])
# valeur de la sublist (= 3ème élément) à l'index 1 (=2ème élément) 
# 20
fruits[2][0] = 30
print("fruits[2] =",fruits[2])
# [30, 20]
print("len(fruits) =", len(fruits))
# 3

# RANGE
print()
print("RANGE")
print("range(4) =", range(4))
# range(0, 4)
print("list(range(4)) =", list(range(4)))
# Output: [0, 1, 2, 3]
print("list(range(len(fruits))) = ", list(range(len(fruits))))
# [0, 1, 2]

# CONCATENATING LISTS
print("CONCATENATING LISTS")
print("Concat with + : list1 + list2")
print("Slicing list with list[1:3]")
stuff = list()
stuff.append("book")
stuff.append("99")
print("Ajouter un élément à la fin de la liste avec .append() :", stuff)
# ['book', '99']
stuff.sort()
print("Trier une liste par odre croissant avec .sort() :", stuff)
# ['99', 'book']
print("max(stuff) : ", max(stuff))
# book

# NUM LIST
# print()
# numlist = list()
# while True:
#     inp = input("Enter a number: ")
#     if inp == "done": break
#     value = float(inp)
#     numlist.append(value)
# average = sum(numlist) / len(numlist)
# print("Average of inputs until 'done' :", average)

# SPLIT LIST
print()
print("SPLIT LIST")
words = 'His e-mail is q-lar@freecodecamp.org'
pieces = words.split()
# découpe à chaque espace trouvé
print(pieces)
# ['His', 'e-mail', 'is', 'q-lar@freecodecamp.org']
parts = pieces[3].split('-')
# découpe à chaque tiret trouvé
n = parts[1]
print(n)
# lar@freecodecamp.org
print('---------------------------------')

# DICTIONARIES
print()
print("DICTIONARIES (MUTABLES)")
print("dict['key'] = value")
dict1 = {"Fri": 20, "Thu": 6, "Sat": 1}
# new name = new entry
dict1["Thu"] = 13
dict1["Sat"] = 2
dict1["Sun"] = 9
print(dict1)
# {'Fri': 20, 'Thu': 13, 'Sat': 2, 'Sun': 9}
print(dict1["Sun"])
# 9

print()
print("get pour simplifier le count et éviter les erreurs si key absente")
counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
# si pas dans le dict, valeur 0 mise par défaut : 
print(counts.get('kris', 0))
# 0
name = "mrugesh"
# if name in counts:
#     x = counts[name]
# else:
#     x = 0
# remplacé par :
x = counts.get(name, 0)
# 0 = valeur par défaut
print(x)
# 42

# Dictionary & loop
print()
print("Loop in dictionary for values > 10 : ")
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
        # mrugesh 42
        # beau 100
print(counts.keys())        
# dict_keys(['quincy', 'mrugesh', 'beau', '0']) 
print(counts.values())
# dict_values([1, 42, 100, 10])
print(counts.items())
# dict_items([('quincy', 1), ('mrugesh', 42), ('beau', 100), ('0', 10)])
for aaa, bbb in counts.items():
    print (aaa, bbb)
    # quincy 1
    # mrugesh 42
    # beau 100
    # 0 10     
print('---------------------------------')

# TUPLES
print()
print("TUPLES (IMMUTABLES)")
t = tuple()
print(dir(t))
# ["count", "index"] (sort, append, reverse.. ne fonctionnent pas)
t = (3, 2, 1)
print(t)
# (3, 2, 1)

(a, b) = (99, 98)
print(a)
# 99
compareTuples = (99, 98) > (1, 2)
print(compareTuples)
# True

d = dict()
d["Hello"] = 2
d["World"] = 4
tups = d.items()
print(tups)
# dict_items([('Hello', 2), ('World', 4)]) 

# Sorting Lists of Tuples
print()
print("Sort by value :")
lst = []
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
print(lst)
# [(100, 'beau'), (42, 'mrugesh'), (10, '0'), (1, 'quincy')]
# same as :
print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )
# [(100, 'beau'), (42, 'mrugesh'), (10, '0'), (1, 'quincy')]

# Comparing & sorting Tuples
print()
print("Comparing & sorting Tuples")
fhand2 = open("lorem.txt")
counts2 = dict()
for line in fhand2:
    words2 = line.split()
    for word2 in words2:
        counts2[word2] = counts2.get(word2, 0) + 1

lst = list()
for key, val in counts2.items():
    newtuple = (val, key)
    lst.append(newtuple)

lst = sorted(lst, reverse=True)

print("The top 5 most common words : ")
for val, key in lst[:5] : 
    print(key, val)
    # Vestibulum 6
    # sit 5
    # libero 5
    # vel 4
    # nec 4
print('---------------------------------')
   
# REGEX
print()
print("REGULAR EXPRESSION")
# import re obligatoire
import re

print("re.search() pour vérifier qu'un string matche avec une regex")
print("re.findall() pour extraire une portion qui matche avec une regex")
print()

print("Example of regex with search() :")
hand = open("lorem.txt")
print("nec in lines & Cras in the start of line : ")
for line in hand:
    line = line.rstrip()
    if re.search("nec", line):
        print("-", line)
        # renvoie les 4 lignes contenant "nec"
    if re.search("^Cras", line):
        print("-", line)
        # renvoie les lignes que si elles commencent par "nec"

print()
print("Example of regex with findall() :")
s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
lst2 = re.findall('\\S+@\\S+', s)
print(lst2)
# ['csev@umich.edu', 'cwen@iupui.edu']

# ASCII
print("En ASCII, la lettre 'A' a la valeur : ", ord("A"))
# 65
print("En ASCII, la lettre 'a' a la valeur : ", ord("a"))
# 97






