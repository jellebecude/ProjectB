import pandas as pd
import json
from tkinter import *
import urllib.request

#zet panda library settings
#globally defined het bronbestand als "steam"
#voor mogelijke directoy problemen op andere apparaten is de website gebruikt
def file_load():
    pd.set_option('display.min_rows', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    global steam
    steam = pd.read_json('https://raw.githubusercontent.com/tijmenjoppe/AnalyticalSkills-student/master/project/data/steam.json')
file_load()


#Zet alles in  een list vanaf een json file url
def list_functie(thing):
    mylist = []
    with urllib.request.urlopen('https://raw.githubusercontent.com/tijmenjoppe/AnalyticalSkills-student/master/project/data/steam.json') as url:
        data = json.loads(url.read().decode())
        for i in data:
            ree = i[thing]
            mylist.append(ree)
    print(mylist)


# Function to do insertion sort
def insertionSort(the_list):
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

    #simpele GUI
#(voorlopig) alleen functioneel
#laat de naam van het eerste spel in het bronbestand zien
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


#sorteer de data
#hier is het als voorbeeld op prijs gesorteerd
def sort():
    steam.sort_values(by=['price'], inplace=True, ascending=True)
    print(steam[['name', 'price']])
sort()

# hallo
# the