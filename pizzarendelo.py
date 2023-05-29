# Hackathon 2023. május
# Készítette: Csontos Roland
# Harmadik feladat: Pizzarendelő chatbot

# A legegyszerűbben tkinterrel tudok ablakokat létrehozni
from tkinter import *


# Ablak stílus elemei
# Először létrehoztam magát az ablakat, és adtam neki egy nevet.
root = Tk()
root.title("Yeskia Pizzéria")

# Ezeknek a színkódoknak később lesz értelme
# csak azért tettem ide, mert gyorsabban tudtam megváltoztatni.
GombHatterSzin = "#f74939"
ChatHatterSzin = "#ebeced"
SzovegSzin = "#000000"

Betutipus = "Helvetica 14"
BetutipusDolt = "Helvetica 14 bold"

# Ezek a listák akkor kellenek amikor a felhasználó végrehajta a "mi a menü" parancsot
menuPizza = ["Sonkás pizza", "Kukoricás pizza", "Hagymás pizza"]
menuFeltet = ["Extra sajt", "Extra kukorica", "Extra sonka"]
menuItalok = ["Pepsi", "Coca Cola", "Fanta"]

# Több köszönést szerettem volna értelmezni, ezért ezekre tud választ adni a chatbot
koszonesek = [
    "szia",
    "heló",
    "jó napot",
    "szép napot",
    "jó estét",
    "szép estét",
    "szevasz",
    "szia!",
    "heló!",
    "jó napot!",
    "szép napot!",
    "jó estét!",
    "szép estét!",
    "szevasz!",
]

# Mivel sokan a számokat betűkkel adják meg, szükség volt egy listára ahol ezeket tudom értelmezni
# Itt szerepelnek számok 'szám' formában (pl.:1,2,3). Ezekre azért volt szükség mert ezeket egészen a rendelés végéig stringként
# kezelem. Csak a végén váltom át int-é.
szamok = [
    "egy",
    "két",
    "kettő",
    "három",
    "négy",
    "öt",
    "hat",
    "hét",
    "nyolc",
    "kilenc",
    "tíz",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]

# A valasztott változó magát a rendelést tartalmazza nehezen értelmezhető formában
# Ezt konvertálom át és mentem el a ValasztottTargyankent változóba akkor, amikor a felhasználó véglegesítette a rendelését.
Valasztott = []
ValasztottTargyankent = []
# A címet azért kellett elmentemem egy külön változóba mert így könnyen tudom ellenőrizni, hogy a felhasználó beírta-e vagy nem.
# Erre a legkönnyebb mód az, hogy ha megnézem a cím lista hosszát. A cím azért lesz lista mert így rendkívül könnyen eltudtam
# távolítani a 'cím' parancsot a szöveg elejéről/végéről.
Cim = []


# Ez a send függvény tulajdonképp mindennek az agya.
def send():
    # Itt visszaállítom a chat ablak állapotát normálra. Így megjelennek benne az üzenetek. A def végén pedig DISABLED
    # állapotra kapcsolom így a felhasználó nem tud beleírni!
    txt.config(state=NORMAL)
    # Erre az egy sorra azért van szükség, hogy megjelöljem melyik üzenetet írta a felhasználó, és melyiket a pizzasegéd.
    # A beküldött üzenet elé csak betettem a "Te:" jelzőt.
    txt.insert(END, "\n" + f"Te: {e.get()}")

    # A user takarja a felhasználó üzenetét. Azért kellett átteni kisbetűsre, mert így akárhogyan írja be a felhasználó
    # (ameddig a parancs helyes) a program megérti őt.
    user = e.get().lower()

    # itt jön be a képbe a hosszú koszonesek lista.
    if user in koszonesek:
        txt.insert(END, "\n" + "Pizzasegéd: Szép napot!")

    # A szeretnék parancs a megrendelés folyamat kezdetét jelenti, alternatív formája a kérek.
    elif "szeretnék" in user or "kérek" in user:
        # A felhasználó üzenetét átalakítom egy listává mert úgy sokkal könnyebb lesz kezelni.
        user = user.strip().split()
        print(user)
        for i in user:
            if i in szamok:
                # Azért rakok beide egy és-t, mivel az később gördülékenyebbé teszi az 'ennyi lesz' parancs lefutását.
                # A rendelés tárgyai úgy kerülnek összeadásra, hogy 1 tárgy az a lista összes eleme két 'és' között.
                Valasztott.append("és")
                Valasztott.append(i)
            elif i == "és" or i == "meg":
                Valasztott.append("és")
            # A következőekben csak szimplán a listához hozzáadom a megfelelő kulcs szavakat. A sok if-el könnyedén letudom szűrni hogy a felhasználó mit szeretne.
            elif i == "sonkás" or i == "kukoricás" or i == "hagymás":
                Valasztott.append(i)
            elif i == "pizza" or i == "pizzát":
                Valasztott.append("pizza")
            elif (
                i == "extra"
                or i == "kukoricával"
                or i == "sajttal"
                or i == "sonkával"
                or i == "hagymával"
            ):
                Valasztott.append(i)
            # Az italokat megírhattam volna külön if-be is, azonban szerintem ez így egy fokkal jobban áttekinthető.
            elif (
                i == "pepsi"
                or i == "coca cola"
                or i == "kóla"
                or i == "fanta"
                or i == "pepsivel"
                or i == "coca colával"
                or i == "kólával"
                or i == "fantával"
                or i == "pepsit"
                or i == "kólát"
                or i == "coca colat"
                or i == "fantát"
            ):
                if i == "pepsi" or i == "pepsivel" or i == "pepsit":
                    Valasztott.append("üveg Pepsi")
                elif (
                    i == "coca Cola"
                    or i == "kóla"
                    or i == "coca colával"
                    or i == "kólával"
                    or i == "coca colat"
                    or i == "kólát"
                ):
                    Valasztott.append("üveg Coca Cola")
                elif i == "fanta" or i == "fantával" or i == "fantát":
                    Valasztott.append("üveg Fanta")
        print(Valasztott)
        txt.insert(END, "\n" + "Pizzasegéd: Rendben, ")
        # A VoltMarEs változó ellenőrzi, hogy két és-t egymás után a program ne írjon ki. Ez abból adódik, hogy a számok elé is beillesztettem egy ést.
        VoltMarEs = False
        for i in Valasztott[1:]:
            if VoltMarEs and i == "és":
                txt.insert(END, "")
            if i == "és" and VoltMarEs == False:
                VoltMarEs = True
                txt.insert(END, f"{i} ")
            elif i != "és":
                VoltMarEs = False
                txt.insert(END, f"{i} ")
        txt.insert(
            END,
            "rendel. \nPizzasegéd: Bármi mást szeretnél?\nHa nem akkor kérlek használd az 'ennyi lesz' parancsot\n",
        )

    # A cím parancsban a felhasználó üzenetét átalakítottam egy listába, és a cím listához csak nem adtam hozzá azokat a szavakat melyek nem a címet képzik.
    elif "cím" in user or "címem" in user:
        user = user.strip().split()
        txt.insert(END, "\n" + "Pizzasegéd: A következő címet mentettem el: ")
        for i in user:
            if i == "a" or i == "cím" or i == "címem":
                pass
            else:
                Cim.append(i)
                txt.insert(END, f"{i} ")
        txt.insert(
            END,
            "\n"
            + "Ha a cím helytelen akkor a parancs újboli beírásával tudod módosítani\n",
        )

    elif "ennyi lesz" in user:
        if len(Valasztott) == 0 or len(Valasztott) == 1:
            # Ha a Valasztott lista hosszúsága 0 az azt jelenti hogy a felhasználó még nem írta be a 'szeretnék' parancsot!
            txt.insert(
                END,
                "\n" + "Pizzasegéd: Kérlek rendelj valamit hogy leadhasd a rendelésed",
            )
        else:
            # Itt a termékeket egy hosszú lista helyett listán belüli listákba helyezem. Ezzel később megkönnyebbítem
            # a termékek árainak meghatározását.
            temp = []
            for i in range(len(Valasztott)):
                # Itt jön be a képbe az és, tulajdonképp mint szóköz játszik szerepet.
                if Valasztott[i] == "és":
                    temp = []
                # Ezzel a sorral biztosra megyek, hogy a rendelés utolsó eleme is véglegesítésre kerül.
                # Ha ezt nem rakom be nagyon ritkán vannak olyan esetek, hogy az utolsó elem lemarad!
                elif Valasztott[i] == Valasztott[-1]:
                    print(Valasztott[i])
                    temp.append(Valasztott[i])
                    ValasztottTargyankent.append(temp)
                    temp = []
                elif (
                    Valasztott[i] == "kukoricás"
                    or Valasztott[i] == "sonkás"
                    or Valasztott[i] == "hagymás"
                ):
                    print(Valasztott[i])
                    temp.append(Valasztott[i])
                    ValasztottTargyankent.append(temp)
                    temp = []
                elif "üveg" in Valasztott[i]:
                    print(Valasztott[i])
                    temp.append(Valasztott[i])
                    ValasztottTargyankent.append(temp)
                    temp = []
                else:
                    temp.append(Valasztott[i])
            print(ValasztottTargyankent)
            txt.insert(END, "\n" + "Pizzasegéd: A rendelésed a következő:\n")
            VoltMarEs = False
            for i in Valasztott[1:]:
                if VoltMarEs and i == "és":
                    txt.insert(END, "")
                if i == "és" and VoltMarEs == False:
                    VoltMarEs = True
                    txt.insert(END, f"{i} ")
                elif i != "és":
                    VoltMarEs = False
                    txt.insert(END, f"{i} ")

            # Itt jön képbe a listában a lista konstrukció
            # Amikor a for ciklusban lefuttatom a ValasztottTargyankent listát, akkor szükség van egy második for ciklusra.
            # Így akár részletezve is kilehet írni az elemek árát, nem csak a végső árat.
            VegsoAr = 0
            for i in ValasztottTargyankent:
                tempSzam = 0
                tempAr = 0
                for x in i:
                    if x == "egy" or x == "1":
                        tempSzam = 1
                    elif x == "két" or x == "kettő" or x == "2":
                        tempSzam = 2
                    elif x == "három" or x == "3":
                        tempSzam = 3
                    elif x == "négy" or x == "4":
                        tempSzam = 4
                    elif x == "öt" or x == "5":
                        tempSzam = 5
                    elif x == "hat" or x == "6":
                        tempSzam = 6
                    elif x == "hét" or x == "7":
                        tempSzam = 7
                    elif x == "nyolc" or x == "8":
                        tempSzam = 8
                    elif x == "kilenc" or x == "9":
                        tempSzam = 9
                    elif x == "tíz" or x == "10":
                        tempSzam = 10
                    elif x == "kukoricás" or x == "sonkás" or x == "hagymás":
                        tempAr = 1800
                    elif "üveg" in x:
                        tempAr = 500
                VegsoAr += tempAr * tempSzam
            print(VegsoAr)
            txt.insert(
                END,
                "\n"
                + f"Pizzasegéd: Összesen {VegsoAr} forintot fog a futár kérni. Ha még nem adtad meg a címed akkor kérlek most tedd meg a 'címem' parancsal!\n",
            )

    elif "megrendelem" in user or "megrendelés" in user:
        print(Cim)
        # Leellenörzöm hogy véglegesítette már a rendelését a felhasználó vagy nem illetve
        # hogy megadta-e a címét.
        if len(ValasztottTargyankent) == 0:
            txt.insert(
                END, "\n" + "Pizzasegéd HIBA: Még nem véglegesítetted a rendelésed!"
            )
        elif len(Cim) == 0:
            txt.insert(END, "\n" + "Pizzasegéd HIBA: Még nem adtad meg a címedet")
        else:
            # Ha minden sikeres akkor a program bezárul 6 másodperc után.
            txt.insert(
                END,
                "\n"
                + "Pizzasegéd: A rendelésed sikeresen leadtad. Köszönjük hogy minket választottál!",
            )
            txt.insert(
                END, "\n" + "Pizzasegéd: Az ablak néhány másodpercen belül bezárul!"
            )
            root.after(6000, lambda: root.destroy())

    # A külön listákba szedett menü elemek itt sokat segítenek, hiszen részletezve tudom kiírni a menüt.
    elif "mi a menü" in user:
        txt.insert(END, "\n" + "Pizzasegéd: A következő termékek érhetőek el nálunk:")
        for i in menuPizza:
            txt.insert(END, "\n" + f"{i}")

        txt.insert(
            END,
            "\n\n"
            + "Pizzasegéd: Extra feltétek és elérhetőek nálunk.\nA következők közül választhatsz: ",
        )
        for i in menuFeltet:
            txt.insert(END, "\n" + f"{i}")

        txt.insert(
            END,
            "\n\n"
            + "Pizzasegéd: Ha esetleg megszomjazol, mi azon is segítünk!\nA következő italok érhetőek el nálunk: ",
        )
        for i in menuItalok:
            txt.insert(END, "\n" + f"{i}")

    # Szimplán csak részletezem a parancsokat.
    # Azért írtam minden parancsot külön txt.insertbe hogy átláthatóbb legyen.
    elif "segítség" in user:
        txt.insert(
            END,
            "\n\n\n\n"
            + "Pizzasegéd: A pizzasegéd egy pizzarendelő automatizált rendszer.\n",
        )
        txt.insert(
            END,
            "\n"
            + "Pizzasegéd: A használatom egyszerű csupán néhány paracsot értek meg:",
        )
        txt.insert(
            END,
            "\n"
            + "Pizzasegéd: A 'mi a menü' parancsra elmondom neked az aktuális menünket.\n",
        )
        txt.insert(
            END,
            "\n"
            + "Pizzasegéd: A 'szeretnék' parancsal tudod a rendelésed összerakni.\nPéldául: szeretnék egy kukoricás pizzát és egy fantát\n",
        )
        txt.insert(
            END,
            "\n"
            + "Pizzasegéd: Ha mindent kiválasztottál akkor az 'ennyi lesz' paranccsal\ntudod véglegesíteni a rendelésed, itt ki is írom hogy mennyibe fog kerülni\n",
        )
        txt.insert(
            END,
            "\n"
            + "Pizzasegéd: A 'címem' paranccsal tudod hozzáadni a címedet a rendeléshez\nPéldául: a címem 1042 Budapest Árpád út 10\n",
        )
        txt.insert(
            END,
            "\n"
            + "Pizzasegéd: A 'megrendelem' paranccsal tudod leadni a rendelésedet!\n",
        )
    # Szimplán csak leakartam reagálni ha a felhasználó elküld egy üres üzenetet.
    elif user == "" or user == " ":
        txt.insert(
            END,
            "\n" + "Pizzasegéd: A rendelés leadásához kérlek írd le mit szeretnél! ",
        )

    # Ha az üzenet tartalmaz valamit, de az egyáltalán nem tudja értelmezni a pizzasegéd akkor ezt adja vissza.
    else:
        txt.insert(
            END,
            "\n"
            + "Pizzasegéd: Ne haragudj nem értem az üzeneted! Megtudnád ismétleni kérlek?",
        )

    # A txt.see szimplán csak legörget a legutolsó üzenetig, elkerülve hogy a felhasználónak keljen görgetni.
    txt.see("end")

    # Itt kapcsolom ki hogy a felhasználónak lehetősége legyen beleírni a chatbox-ba, így csak az Entry mező elérhető
    txt.config(state=DISABLED)
    e.delete(0, END)


# A következő részben jön nagyon jól a Betitupus, BetutipusDolt, a ChatHatterSzin és a SzovegSzin változó.

# Ezzel kirakom a pizzéria nevét az ablak felső közép részére.
PizzeriaNeve = Label(
    root,
    fg=SzovegSzin,
    text="Yeskia Pizzéria",
    font=BetutipusDolt,
    pady=10,
    width=20,
    height=1,
).grid(row=0, column=0)

# Itt létrehozom a fő text gridet, ebben jellennek meg az üzenetek.
txt = Text(root, bg=ChatHatterSzin, fg=SzovegSzin, font=Betutipus, width=60, height=15)
txt.grid(row=1, column=0, columnspan=2)

# Ez pedig a chat entry mező, azaz itt írja be a felhasználó az üzenetét.
e = Entry(root, bg="#ffffff", fg=SzovegSzin, font=Betutipus, width=55)
e.grid(row=2, column=0)

KuldesGomb = Button(
    root, text="Küldés", font=BetutipusDolt, bg=GombHatterSzin, fg="white", command=send
).grid(row=2, column=1)

# Ez a rövid üzenet azért kell, mivel azt szeretném, hogy minden induláskor megjelenjen.
txt.insert(
    END,
    "Pizzasegéd: Szép napot! Miben segíthetek?\n\nHa segítségre van szükséged a parancsokkal kapcsolatban akkor kérlek írd be a 'segítség' parancsot!",
)
root.wm_iconbitmap('favicon.ico')
root.mainloop()
