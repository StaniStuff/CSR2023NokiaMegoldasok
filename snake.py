# Hackathon 2023. május
# Készítette: Csontos Roland
# Első feladat: Snake játék

from random import randint
from time import sleep
from datetime import date

# A pálya szélességét, és magasságát inkább itt hoztam létre változóként, mivel így a pálya mérete könnyen növelhető.
PalyaSzelesseg = 60
PalyaMagassag = 30

# Ide azért kell +1 mivel a játszható teret szerettem volna 60x30-asra megcsinálni.
KigyoPozicio = [randint(1, PalyaSzelesseg + 1), randint(1, PalyaMagassag + 1)]
PontPozicio = [randint(1, PalyaSzelesseg + 1), randint(1, PalyaMagassag + 1)]
pontok = 0

# Ennek a változónak akkor lesz értelme, amikor a játékos elmenti a játékát.
FelhasznaloNev = ""

# Később a parancsok ellenörzésénel hasznos lesz
JatekParancsok = ["jobbra", "balra", "fel", "le", "meguntam"]


def JatekCim():
    # A sok sortörés segít hogy ne lássák felgörgetés nélkül a játék előző állapotát
    for e in range(50):
        print()
    print(
        r"""
      _____             _        
     / ____|           | |       
    | (___  _ __   __ _| | _____ 
     \___ \| '_ \ / _` | |/ / _ \
     ____) | | | | (_| |   <  __/
    |_____/|_| |_|\__,_|_|\_\___|
      """
    )
    print("    Készítette: Csontos Roland")
    print(f"    Pontjaid: {pontok}\n")


def PontMentes(pont, felsznev):
    with open("eredmeny.txt", "a", encoding="utf-8") as f:
        f.write(f"Játékos: {felsznev}, pontok: {pont}, dátum: {date.today()}\n")
    f.close()


# Játéktér létrehozása
# Defként hoztam létre, mivel így könnyebb lesz meghívni a while ciklusban később.
def JatekTer(x, y, sz, m, px, py):
    # Az x, és y a kigyó pozíciója, az sz és m pedig a pálya szélessége és magassága. A px és a py a pont
    # koordinátáit jelzi.

    # A játék végét jelző külön változóra azért volt szükség, mivel így kitudom rajzolni az egész pályát,
    # mielőtt a program kilép
    Vége = False
    # A játéktér tetejének printje A magassághoz azért adtam hozzá hármat, hogy a pálya ténylegesen 30 magas legyen ne
    # pedig 28. Azért hármat mert a kettő határ elfoglal két sort, és a for ciklus 0-tól megy nem 1-től.
    for i in range(m + 3):
        # Ellenőrzöm, hogy az i nem-e az első vagy utolsó szám a for ciklusban, mivel azok a játéktér tetejét és szélét jelzik.
        if i == 0:
            # Úgy mint a magassághoz, a szélességhez is szükség volt +3-ra, hogy a pálya ténylegesen elérje a kívánt méretet.
            for a in range(sz + 2):
                if a == x and y == 0:
                    print("@", end="")
                    Vége = True

                else:
                    print("*", end="")
            # A for ciklus végén szükség van egy sortöréses karakterre, és ez volt a legegyszerűbb mód.
            print("*")

        elif i == m + 2:
            for b in range(sz + 2):
                if b == x and y == m + 2:
                    print("@", end="")
                    Vége = True

                else:
                    print("*", end="")
            print("*")

        # Amikor egy sorban van a pont, és a kígyó akkor ezzel tudom megjeleníteni
        elif i == y and i == py:
            if x == 0:
                print("@", end="")
                Vége = True
                for g in range(1, sz + 3):
                    if g == sz + 2:
                        print("*")
                    else:
                        print(" ", end="")

            elif x == sz + 2:
                Vége = True
                for f in range(sz + 2):
                    if f == 0:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("@")

            # Amikor a koordinátájuk ugyen az akkor szükség van erre, máskülönben semelyik sem jelenik meg.
            elif x == px:
                for c in range(sz + 2):
                    # Itt pedig x kordináta alapján keresem meg a pálya szélességében.
                    if c == x:
                        print("@", end="")
                    elif c == 0:
                        print("*", end="")
                    elif c != 0 or c != x:
                        print(" ", end="")
                print("*")

            else:
                for c in range(sz + 2):
                    # Itt pedig x kordináta alapján keresem meg a pálya szélességében.
                    if c == x:
                        print("@", end="")
                    elif c == px:
                        print("x", end="")
                    elif c == 0:
                        print("*", end="")
                    elif c != 0 or c != x:
                        print(" ", end="")
                print("*")

        # A következő ciklusban printelem ki a kígyót, amikor nincsen egy sorban a ponttal.
        # Először is az y kordinátája alapján keresem meg a magasságbeli elhelyezkedését, mivel a játékot soronként printelem ki.
        elif i == y:
            # Ha a kígyó a 0. vagy utolsó elemre esik akkor vége a játéknak, akkor üti meg a falat, ezért ezt ellenörzöm először.
            if x == 0:
                print("@", end="")
                Vége = True
                for g in range(1, sz + 3):
                    if g == sz + 2:
                        print("*")
                    else:
                        print(" ", end="")

            elif x == sz + 2:
                Vége = True
                for i in range(sz + 2):
                    if i == 0:
                        print("*", end="")
                    else:
                        print(" ", end="")
                print("@")

            else:
                for c in range(sz + 2):
                    # Itt pedig x kordináta alapján keresem meg a pálya szélességében.
                    if c == x:
                        print("@", end="")
                    elif c == 0:
                        print("*", end="")
                    elif c != 0 or c != x:
                        print(" ", end="")
                print("*")

        elif i == py:
            for c in range(sz + 2):
                # Itt pedig x kordináta alapján keresem meg a pálya szélességében.
                if c == px:
                    print("x", end="")
                elif c == 0:
                    print("*", end="")
                elif c != 0 or c != x:
                    print(" ", end="")
            print("*")

        # Ha a sorban nincsen benne a kígyó akkor pedig csak ez fut le.
        elif i != y or i != 0 or i != m + 1:
            for t in range(sz + 2):
                if t == 0:
                    print("*", end="")
                elif t > 0:
                    print(" ", end="")
            print("*")

    if Vége:
        FelhasznaloNev = str(input("Kérlek írd be a felhasználónevedet a pontjaid elmentéséhez! Ha nem szeretnéd elmenteni az állásodat akkor nyomj egy entert! "))
        if len(FelhasznaloNev) > 0:
            PontMentes(pontok, FelhasznaloNev)
        print("Most ennyi volt, szép napot!")
        quit()


# Azért nem a while ciklus elején írom ki mindig hiszen a mozgások után mindig már kiprintelem egyszer.
# Ezzel elkerültem hogy az utolsó lépést kétszer mutassa a játék
JatekCim()
JatekTer(KigyoPozicio[0], KigyoPozicio[1], PalyaSzelesseg, PalyaMagassag, PontPozicio[0], PontPozicio[1])

while True:
    # A .lower() hasznos mivel így a játékos bárhogyan beírjatja az irányszavakat a programnak mindig csak a kisbetűs irányszót kell ellenőriznie.
    # Ha átalakítjuk az inputot egy listává, akkor egyszerre több irány parancsot tudunk értelmezni sorban.
    hova = str(input("Hova? ")).lower().strip().split()

    ParancsEllenorzes = False
    while not ParancsEllenorzes:

        # A változó a helyes parancsokat számolja, így csak akkor enged tovább lépni ha minden parancs helyes.
        helyes = 0

        # A for ciklussal több parancsot is ellenörzök nem csak egyet
        for i in range(len(hova)):
            if hova[i] in JatekParancsok:
                helyes += 1
            else:
                # Inkább kiírom a hibás parancsot, hogy a felhasználó is lássa.
                ideiglenes = str(input(f"Nem értem ezt a parancsot: '{hova[i]}'. Kérlek letudnád írni újra? "))
                hova[i] = ideiglenes

                # Hibás parancs esetén az egészet nullázom, és újra ellenörzöm addig, ameddig mindegyik helyes nem lesz.
                helyes = 0

        if helyes == len(hova):
            ParancsEllenorzes = True

    for i in hova:
        if i == "jobbra":
            KigyoPozicio[0] = int(KigyoPozicio[0]) + 1
            if KigyoPozicio[0] == PontPozicio[0] and KigyoPozicio[1] == PontPozicio[1]:
                pontok += 1
                PontPozicio = [randint(1, PalyaSzelesseg), randint(1, PalyaMagassag)]
            JatekCim()
            JatekTer(KigyoPozicio[0], KigyoPozicio[1], PalyaSzelesseg, PalyaMagassag, PontPozicio[0], PontPozicio[1])
            # A sleepet azért raktam ide mert akkor jobban néz ki a karakter mozgása.
            sleep(0.3)

        elif i == "balra":
            KigyoPozicio[0] = int(KigyoPozicio[0]) - 1

            # Összehasonlítom a pont és a kigyónak a helyét, mivel itt egyszerűbb mint a játéktér függvényben.
            if KigyoPozicio[0] == PontPozicio[0] and KigyoPozicio[1] == PontPozicio[1]:
                pontok += 1
                PontPozicio = [randint(1, PalyaSzelesseg), randint(1, PalyaMagassag)]
            JatekCim()
            JatekTer(KigyoPozicio[0], KigyoPozicio[1], PalyaSzelesseg, PalyaMagassag, PontPozicio[0], PontPozicio[1])
            # A sleepet azért raktam ide mert akkor jobban néz ki a karakter mozgása.
            sleep(0.3)

        elif i == "fel":
            KigyoPozicio[1] = int(KigyoPozicio[1]) - 1
            if KigyoPozicio[0] == PontPozicio[0] and KigyoPozicio[1] == PontPozicio[1]:
                pontok += 1
                PontPozicio = [randint(1, PalyaSzelesseg), randint(1, PalyaMagassag)]
            JatekCim()
            JatekTer(KigyoPozicio[0], KigyoPozicio[1], PalyaSzelesseg, PalyaMagassag, PontPozicio[0], PontPozicio[1])
            # A sleepet azért raktam ide mert akkor jobban néz ki a karakter mozgása.
            sleep(0.3)

        elif i == "le":
            KigyoPozicio[1] = int(KigyoPozicio[1]) + 1
            if KigyoPozicio[0] == PontPozicio[0] and KigyoPozicio[1] == PontPozicio[1]:
                pontok += 1
                PontPozicio = [randint(1, PalyaSzelesseg), randint(1, PalyaMagassag)]
            JatekCim()
            JatekTer(KigyoPozicio[0], KigyoPozicio[1], PalyaSzelesseg, PalyaMagassag, PontPozicio[0], PontPozicio[1])
            # A sleepet azért raktam ide mert akkor jobban néz ki a karakter mozgása.
            sleep(0.3)

        elif i == "meguntam":
            FelhasznaloNev = str(input("Kérlek írd be a felhasználónevedet a pontjaid elmentéséhez! Ha nem szeretnéd elmenteni az állásodat akkor nyomj egy entert! "))
            if len(FelhasznaloNev) == 0:
                quit()
            else:
                PontMentes(pontok, FelhasznaloNev)
                quit()