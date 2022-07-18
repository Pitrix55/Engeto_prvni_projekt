"""
TEXTOVÝ ANALYZÁTOR

projekt_1.py: První projekt do Engeto Online Python Akademie

author: Petr Vodák
email: vodak.petr10@seznam.cz
discord: Pitrix#0619
"""

import task_template

users = {"bob" : "123", "ann" : "pass123", "mike" : "password123", "liz" : "pass123"}

# vstupy, které vyžádají přihlašovací údaje
nickname = input("username: ")
password = input("password: ")
oddelovac = "-"*40

print(oddelovac)

# kontrola, zda je uživatel v databázi a zadal správně heslo, jinak ukončení
if nickname in users and users[nickname] == password:
    print(f"Welcome to the app, {nickname}")
else:
    print("unregistered user, terminating the program..")
    exit()

print("We have 3 texts to be analyzed.", oddelovac, sep="\n")

# vstup, kterým uživatel vybere text k analýze, špatný vstup -> ukončení
vyber_textu = input("Enter a number btw. 1 and 3 to select: ")

if vyber_textu == "1" or vyber_textu == "2" or vyber_textu == "3":
    text = task_template.TEXTS[int(vyber_textu)-1]

else:
    print("You must enter a digit between 1 and 3!")
    exit()

print(oddelovac)

# rozdělení textu podle mezer a očištění slov od nevyžádaných znaků
cisty_text = list()
for slovo in text.split():
    cisty_text.append(slovo.strip('.').strip(','))
   

pocet_slov = len(cisty_text)
title_word = 0
upper_word = 0
lower_word = 0
digit = list()

# zjištění, o jaký typ slova se jedná a zaznamenání počtu
for slovo in cisty_text:
    if slovo.istitle():
        title_word += 1
    elif slovo.isupper():
        upper_word += 1
    elif slovo.islower():
        lower_word += 1
    elif slovo.isdigit():
        digit.append(int(slovo))
        number = len(digit)
        suma = sum(digit)

print(f"""There are {pocet_slov} words in the selected text.
There are {title_word} titlecase words.
There are {upper_word} uppercase words.
There are {lower_word} lowercase words.
There are {number} numeric strings.
The sum of all the numbers {suma}""", oddelovac, sep='\n')

print("LEN|","OCCURENCES".center(15),"|NR.")
print(oddelovac)

# rozdělení slov podle délky a zaznamenání počtu
delka_slov = dict()
for slovo in cisty_text:
    if len(slovo) in delka_slov:
        delka_slov[len(slovo)] += 1
    else:
        delka_slov[len(slovo)] = 1

# seřazení slov podle délky (od nejmenšího) a vypsání pouze počtu slov daných délek
upravena_delka_slov = list()
for slovo in sorted(delka_slov.items()):
    upravena_delka_slov.append(slovo[1])

# přiřazení indexu (od 1) délek k četnosti výskytu a zapsání do sloupcového grafu
for delka, pocet in enumerate(upravena_delka_slov,1):
    print(f"{delka:>3}|{'*'*pocet+(17-pocet)*' '}|{pocet}")