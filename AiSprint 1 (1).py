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


# Zet alles in  een list vanaf een json file url
def list_functie(thing, thing2):
    listone = []
    listtwo = []
    with urllib.request.urlopen(
            'https://raw.githubusercontent.com/tijmenjoppe/AnalyticalSkills-student/master/project/data/steam.json') as url:
        data = json.loads(url.read().decode())
        for i in data:
            naam = i[thing]
            prijs = i[thing2]
            listone.append(naam)
            listtwo.append(prijs)
    return listone, listtwo


list_functie("name", "price")


def pricesort():
    naamlijst = []
    prijslijst = []
    with urllib.request.urlopen(
            'https://raw.githubusercontent.com/tijmenjoppe/AnalyticalSkills-student/master/project/data/steam.json') as url:
        data = json.loads(url.read().decode())
        for i in data:
            naam = i["name"]
            prijs = i["price"]
            naamlijst.append(naam)
            prijslijst.append(prijs)

    omgewisseld = True
    while omgewisseld:
        omgewisseld = False
        for x in range(len(prijslijst) - 1):  # aantal elementen in lijst
            if prijslijst[x] > prijslijst[x + 1]:
                prijslijst[x], prijslijst[x + 1] = prijslijst[x + 1], prijslijst[x]
                naamlijst[x], naamlijst[x + 1] = naamlijst[x + 1], naamlijst[x]
                omgewisseld = True

    for x in range(len(prijslijst)):
        print(naamlijst[x], prijslijst[x])


pricesort()


# Function to do insertion sort
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

    # simpele GUI


# (voorlopig) alleen functioneel
# laat de naam van het eerste spel in het bronbestand zien
def gui():
    screen = Tk()
    screen.geometry("480x270")

    label1 = Label(
        master=screen,
        text=steam[['name']].head(1),
    )
    label1.pack()

    screen.mainloop()


gui()


# sorteer de data
# hier is het als voorbeeld op prijs gesorteerd
def sort():
    steam.sort_values(by=['price'], inplace=True, ascending=True)
    print(steam[['name', 'price']])
