# Hackathon 2023. május
# Készítette: Csontos Roland
# Második feladat: Dobble Generátor


from itertools import combinations
from random import shuffle

print(r""" 
 _____        _     _     _         _____                       __  _             
|  __ \      | |   | |   | |       / ____|                     /_/ | |            
| |  | | ___ | |__ | |__ | | ___  | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
| |  | |/ _ \| '_ \| '_ \| |/ _ \ | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
| |__| | (_) | |_) | |_) | |  __/ | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
|_____/ \___/|_.__/|_.__/|_|\___|  \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
""")
print("Készítette: Csontos Roland\n")

print("FIGYELEM: 6-nál nagyobb szám Dobble paklijának kiszámítása jelentős számítógépes erőforrást igényel,")
print("illetve még akkor is több időbe telik!\n")
EgyKartyanHanySzam = input("Kérlek add meg hány számn lehet egy kártyán: ")

EgyKartyanHanySzamHelyes = False

while EgyKartyanHanySzamHelyes:
    try:
        int(EgyKartyanHanySzam)
        EgyKartyanHanySzamHelyes = True
    except ValueError:
        print("FIGYELEM: 6-nál nagyobb szám Dobble paklijának kiszámítása jelentős számítógépes erőforrást igényel,")
        print("illetve még akkor is több időbe telik!\n")
        EgyKartyanHanySzam = input("Kérlek egy értelmezhető számot adj meg! ")

EgyKartyanHanySzam = int(EgyKartyanHanySzam)
MaxKartya = input(f"Kérlek add meg hogy hány számot lehet felhasználni. A legkisebb érték amit megtudsz adni az {(EgyKartyanHanySzam ** 2) - EgyKartyanHanySzam}. ")
MaxKartyaHelyes = False
while MaxKartyaHelyes == False:
    try:
        int(MaxKartya)
        MaxKartya = int(MaxKartya)+1
        if MaxKartya >= (EgyKartyanHanySzam ** 2) - EgyKartyanHanySzam:
            MaxKartyaHelyes = True
        else:
            MaxKartya = input(
                f"Kérlek egy értelmezhető számot adj meg ami legalább {(EgyKartyanHanySzam ** 2) - EgyKartyanHanySzam}. ")
    except ValueError:
        MaxKartya = input(f"Kérlek egy értelmezhető számot adj meg ami legalább {(EgyKartyanHanySzam ** 2) - EgyKartyanHanySzam}. ")

Pakli = []
Kartyak = []
while len(Kartyak) < MaxKartya-1:

    LehetsegesKombinaciok = list(combinations(range(MaxKartya), EgyKartyanHanySzam))
    shuffle(LehetsegesKombinaciok)

    Kartyak = [set(LehetsegesKombinaciok[0])]

    for kombinacio in LehetsegesKombinaciok:
        HelyesKombinacio = True
        KombinacioKeszlet = set(kombinacio)
        for card in Kartyak:
            if not len(card.intersection(KombinacioKeszlet)) == 1:
                HelyesKombinacio = False
                break
        if HelyesKombinacio:
            Kartyak.append(KombinacioKeszlet)

    Kartyak = [list(Kartya) for Kartya in Kartyak]
    print("A program dolgozik a megoldáson. A feladat megoldása beletellhet egy percbe.")

    Pakli.append(Kartyak)

for i in Pakli:
    for x in i:
        for b in x[:-1]:
            print(b, end=" ")
        print(x[-1])