import pandas as pd
import json
from tkinter import *


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
#reeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee
# help me
# test
#ther
# welkom
# the
#th e
##################
#test reeeeeeee