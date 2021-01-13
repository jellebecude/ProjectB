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
    # print(sortedprijs)


def gemiddelde(lijst):
    items = len(lijst)
    totaal = 0
    for item in lijst:
        totaal = totaal + item[0]
    gem = (totaal / items)
    return round(gem)


def freq(lijst):    # returns hoevaak iets terugkomt
    newlst = []
    for items in lijst:
        newlst.append(items[0])
    freqs = {x: newlst.count(x) for x in newlst}    # getal : aantal voorkomens
    return freqs


def modes(lijst):   # returnt wat het meeste voorkomt
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


# pricesort_new()


def genresort_new():
    pijslist = list_functie("genres", "name")
    sortedprijs = insertionsort(pijslist)
    return sortedprijs


def devsort_new():
    pijslist = list_functie("developer", "name")
    sortedprijs = insertionsort(pijslist)
    return sortedprijs


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
            text='hoe wil je de developers sorteren?'
        )
        infolabel.pack(side=TOP)

        lijstlabel = Label(
            master=developersortwindow,
            text=''
        )
        lijstlabel.pack(side=TOP)

        knoppen = Frame(developersortwindow)
        knoppen.pack(side=BOTTOM)

        def alphasort():
            lijstlabel.config(text='sort placeholde')
        alphabetische = Button(
            master=knoppen,
            text='sorteer op alphabetische volgorde',
            command=alphasort
        )
        alphabetische.pack()

        def reversealphasort():
            lijstlabel.config(text='reversesort placeholder')
        reversedalphabetische = Button(
            master=knoppen,
            text='sorteer op alphabetische volgorde omgedraaid',
            command=reversealphasort
        )
        reversedalphabetische.pack()

        def modus():
            devlist = list_functie("developer", "name")
            modus = counter(devlist)
            lijstlabel.config(text=modus)
        meestvoorkomend = Button(
            master=knoppen,
            text='sorteer op meest voorkomend',
            command=modus
        )
        meestvoorkomend.pack()

        def nietmodus():
            lijstlabel.config(text='niet modus sort placeholder')
        minstvoorkomend = Button(
            master=knoppen,
            text='sorteer op minst voorkomend',
            command=nietmodus
        )
        minstvoorkomend.pack()

    def genresort():
        genresortwindow = Toplevel(screen)
        genresortwindow.title('sorteren op genres')
        genresortwindow.geometry('500x500')

        infolabel = Label(
            master=genresortwindow,
            text='hoe wil je de genres sorteren?'
        )
        infolabel.pack(side=TOP)

        lijstlabel = Label(
            master=genresortwindow,
            text=''
        )
        lijstlabel.pack(side=TOP)

        knoppen = Frame(genresortwindow)
        knoppen.pack(side=BOTTOM)

        def alphasort():
            lijstlabel.config(text='alphasort placeholder')
        alphabetische = Button(
            master=knoppen,
            text='sorteer op alphabetische volgorde',
            command=alphasort
        )
        alphabetische.pack()

        def reversealphasort():
            lijstlabel.config(text='reverse alphasort placeholder')
        reversedalphabetische = Button(
            master=knoppen,
            text='sorteer op alphabetische volgorde omgedraaid',
            command=reversealphasort
        )
        reversedalphabetische.pack()

        def modus():
            lijstlabel.config(text='modus placeholder')
        meestvoorkomend = Button(
            master=knoppen,
            text='sorteer op meest voorkomend',
            command=modus
        )
        meestvoorkomend.pack()

        def nietmodus():
            lijstlabel.config(text='niet modus placeholder')
        minstvoorkomend = Button(
            master=knoppen,
            text='sorteer op minst voorkomend',
            command=nietmodus
        )
        minstvoorkomend.pack()

    label1 = Label(
        master=screen,
        text=steam[['name']].head(1),
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

    screen.mainloop()


gui()


# sorteer de data
# hier is het als voorbeeld op prijs gesorteerd
def sort():
    steam.sort_values(by=['price'], inplace=True, ascending=True)
    print(steam[['name', 'price']])
