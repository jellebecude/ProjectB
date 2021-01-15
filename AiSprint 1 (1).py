import pandas as pd
import json
from tkinter import *
import urllib.request


# zet panda library settings
# globally defined het bronbestand als "steam"
# voor mogelijke directoy problemen op andere apparaten is de website gebruikt
def file_load():
    pd.set_option('display.min_rows', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    global steam
    steam = pd.read_json(
        'https://raw.githubusercontent.com/tijmenjoppe/AnalyticalSkills-student/master/project/data/steam.json')


file_load()


def insertionsort(the_list):
    # Traverse through 1 to len(arr)
    for i in range(1, len(the_list)):
        key = the_list[i]
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < the_list[j]:
            the_list[j + 1] = the_list[j]
            j -= 1
        the_list[j + 1] = key
    return the_list


# Zet alles in  een list vanaf een json file url
def list_functie(thing1, thing2):
    listone = []
    with urllib.request.urlopen(
            'https://raw.githubusercontent.com/tijmenjoppe/AnalyticalSkills-student/master/project/data/steam.json') as url:
        data = json.loads(url.read().decode())
        # print(sorted(data, key = lambda i: (i['name'])))
        for i in data:
            naam = i[thing1], i[thing2]
            listone.append(naam)
    return listone


def pricesort_new():
    pijslist = list_functie("price", "name")
    sortedprijs = insertionsort(pijslist)
    return sortedprijs


def gemiddelde(lijst):
    items = len(lijst)
    totaal = 0
    for item in lijst:
        totaal = totaal + item[0]
    gem = (totaal / items)
    return round(gem)


def freq(lijst):  # returns hoevaak iets terugkomt
    newlst = []
    for items in lijst:
        newlst.append(items[0])
    freqs = dict()
    for i in newlst:
        if i in freqs:
            freqs[i] += 1
        else:
            freqs[i] = 1

    return freqs

    # getal : aantal voorkomens


def modes(lijst):  # returnt wat het meeste voorkomt
    modi = []
    waardes = freq(lijst)
    grootste = 0
    for waarde in waardes.values():
        if waarde > grootste:
            grootste = waarde

    for key, value in waardes.items():
        if value == grootste:
            modi.append(key)
    return sorted(modi)


def mini(lijst):
    return lijst[0]


def maxi(lijst):
    return lijst[-1]


def genresort_new():
    genrelist = list_functie("genres", "name")
    sortedlist = insertionsort(genrelist)
    return sortedlist


def devsort_new():
    devlist = list_functie("developer", "name")
    sortedlist = insertionsort(devlist)
    return sortedlist


def positive_ratings():
    pijslist = list_functie("positive_ratings", "name")
    sortedprijs = insertionsort(pijslist)
    return sortedprijs


def negative_ratings():
    pijslist = list_functie("negative_ratings", "name")
    sortedprijs = insertionsort(pijslist)
    return sortedprijs


def owners():
    pijslist = list_functie("owners", "name")
    sortedprijs = insertionsort(pijslist)
    return sortedprijs


def frequencysort(lijst):  # returned lijst gesorteerd op meest voorkomende
    waardes = freq(lijst)
    for i in waardes.values():
        key = lijst[i]
        j = i - 1
        while j >= 0 and key < lijst[j]:
            lijst[j + 1] = lijst[j]
            j -= 1
        lijst[j + 1] = key
    return lijst


# Function to do insertion sort


# (voorlopig) alleen functioneel
# laat de naam van het eerste spel in het bronbestand zien
def gui():
    screen = Tk()
    screen.geometry("480x270")

    def developersort():
        developersortwindow = Toplevel(screen)
        developersortwindow.title('sorteren op developer')
        developersortwindow.geometry('500x500')

        infolabel = Label(
            master=developersortwindow,
            text='Hoe wil je de developers sorteren?'
        )
        infolabel.pack(side=TOP)

        lijstlabel = Listbox(
            master=developersortwindow,
            width=80
        )
        lijstlabel.pack(side=TOP)

        knoppen = Frame(developersortwindow)
        knoppen.pack(side=BOTTOM)

        def alphasort():
            lijstlabel.delete(0, END)
            sortedlist = devsort_new()
            for i in sortedlist:
                lijstlabel.insert(END, i)

        alphabetische = Button(
            master=knoppen,
            text='Sorteer op alphabetische volgorde A-Z',
            command=alphasort
        )
        alphabetische.pack()

        def reversealphasort():
            lijstlabel.delete(0, END)
            sortedlist = devsort_new()
            omgedraaid = reversed(sortedlist)
            for i in omgedraaid:
                lijstlabel.insert(END, i)

        reversedalphabetische = Button(
            master=knoppen,
            text='Sorteer op alphabetische volgorde Z-A',
            command=reversealphasort
        )
        reversedalphabetische.pack()

        def modus():
            lijstlabel.delete(0, END)
            devlist = list_functie("developer", "name")
            modussort = frequencysort(devlist)
            # controlesort = sorted(freq(devlist).items(), key=lambda x: x[1], reverse=True)
            # for i in controlesort:
            #    print(i[0], i[1])
            for i in modussort:
                lijstlabel.insert(END, i)

        meestvoorkomend = Button(
            master=knoppen,
            text='Sorteer op meest voorkomend',
            command=modus
        )
        meestvoorkomend.pack()

        def nietmodus():
            lijstlabel.delete(0, END)
            devlist = list_functie('developer', 'name')
            modussort = reversed(frequencysort(devlist))
            for i in modussort:
                lijstlabel.insert(END, i)

        minstvoorkomend = Button(
            master=knoppen,
            text='Sorteer op minst voorkomend',
            command=nietmodus
        )
        minstvoorkomend.pack()

    def genresort():
        genresortwindow = Toplevel(screen)
        genresortwindow.title('sorteren op genre')
        genresortwindow.geometry('500x500')

        infolabel = Label(
            master=genresortwindow,
            text='Hoe wil je de genres sorteren?'
        )
        infolabel.pack(side=TOP)

        lijstlabel = Listbox(
            master=genresortwindow,
            width=80
        )
        lijstlabel.pack(side=TOP)

        knoppen = Frame(genresortwindow)
        knoppen.pack(side=BOTTOM)

        def alphasort():
            lijstlabel.delete(0, END)
            sortedlist = genresort_new()
            for i in sortedlist:
                lijstlabel.insert(END, i)

        alphabetische = Button(
            master=knoppen,
            text='Sorteer op alphabetische volgorde A-Z',
            command=alphasort
        )
        alphabetische.pack()

        def reversealphasort():
            lijstlabel.delete(0, END)
            sortedlist = genresort_new()
            omgedraaid = reversed(sortedlist)
            for i in omgedraaid:
                lijstlabel.insert(END, i)

        reversedalphabetische = Button(
            master=knoppen,
            text='Sorteer op alphabetische volgorde Z-A',
            command=reversealphasort
        )
        reversedalphabetische.pack()

        def modus():
            lijstlabel.delete(0, END)
            genrelist = list_functie("genres", "name")
            modussort = frequencysort(genrelist)
            # controlesort = sorted(freq(devlist).items(), key=lambda x: x[1], reverse=True)
            # for i in controlesort:
            #    print(i[0], i[1])
            for i in modussort:
                lijstlabel.insert(END, i)

        meestvoorkomend = Button(
            master=knoppen,
            text='Sorteer op meest voorkomend',
            command=modus
        )
        meestvoorkomend.pack()

        def nietmodus():
            lijstlabel.delete(0, END)
            genrelist = list_functie('genres', 'name')
            modussort = reversed(frequencysort(genrelist))
            for i in modussort:
                lijstlabel.insert(END, i)

        minstvoorkomend = Button(
            master=knoppen,
            text='Sorteer op minst voorkomend',
            command=nietmodus
        )
        minstvoorkomend.pack()

    def pricesort():
        pricesortwindow = Toplevel(screen)
        pricesortwindow.title('sorteren op developer')
        pricesortwindow.geometry('500x500')

        infolabel1 = Label(
            master=pricesortwindow,
            text='Hoe wil je de prijs sorteren?'
        )
        infolabel1.pack(side=TOP)

        lijstlabel = Listbox(
            master=pricesortwindow,
            width=80
        )
        lijstlabel.pack(side=TOP)

        knoppen = Frame(pricesortwindow)
        knoppen.pack(side=BOTTOM)

        def posrate():
            lijstlabel.delete(0, END)
            sortedlist = reversed(positive_ratings())
            for i in sortedlist:
                lijstlabel.insert(END, i)

        alphabetische = Button(
            master=knoppen,
            text='Sorteer op positive ratings',
            command=posrate
        )
        alphabetische.pack()

        def negrate():
            lijstlabel.delete(0, END)
            sortedlist = negative_ratings()
            for i in sortedlist:
                lijstlabel.insert(END, i)

        reversedalphabetische = Button(
            master=knoppen,
            text='Sorteer op negative ratings',
            command=negrate
        )
        reversedalphabetische.pack()

        def prijs():
            lijstlabel.delete(0, END)
            sortedlist = pricesort_new()
            test = reversed(sortedlist)
            for i in test:
                lijstlabel.insert(END, i)

        meestvoorkomend = Button(
            master=knoppen,
            text='Sorteer van duur naar goedkoop',
            command=prijs
        )
        meestvoorkomend.pack()

        def prijs2():
            lijstlabel.delete(0, END)
            sortedlist = pricesort_new()
            for i in sortedlist:
                lijstlabel.insert(END, i)

        minstvoorkomend = Button(
            master=knoppen,
            text='Sorteer van goedkoop naar duur',
            command=prijs2
        )
        minstvoorkomend.pack()

        def eigenar():
            lijstlabel.delete(0, END)
            sortedlist = reversed(owners())
            for i in sortedlist:
                lijstlabel.insert(END, i)

        eigenaren = Button(
            master=knoppen,
            text="Sorteer op aantal bezitters",
            command=eigenar
        )
        eigenaren.pack()

    label1 = Label(
        master=screen,
        text="Welkom",
        font=("NS Sans", 20)
    )
    label1.pack()

    devsortbutton = Button(
        master=screen,
        text='sorteer op developer',
        command=developersort
    )
    devsortbutton.pack(side=LEFT)

    genresortbutton = Button(
        master=screen,
        text='sorteer op genre',
        command=genresort
    )
    genresortbutton.pack(side=RIGHT)

    genresortbutton = Button(
        master=screen,
        text='sorteer op prijs',
        command=pricesort
    )
    genresortbutton.pack(side=BOTTOM)

    screen.mainloop()


gui()


# sorteer de data
# hier is het als voorbeeld op prijs gesorteerd
def sort():
    steam.sort_values(by=['price'], inplace=True, ascending=True)
    print(steam[['name', 'price']])
