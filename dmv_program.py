#Calvin Comstock-Fisher
#1/11/20
#DMV Program GUI

#Step 1: Import Libraries
import tkinter as tk
import sys

#Step 2: Make database for storing people
database = {"D12345":("Addison Cho", 11),"D67890":("Riley McGrath", 8),"H45678":("Charles Morgan",2),"K23456":("Lathika Potnuru",10),"C90123":("Jordan Ruberts", 5),"P78901":("Natalie Scholz", 150),"A34567":("Alan Urbonavicius",210),"P56789":("Alan Zhang",4)}

#Step 3: Make the tkinter window and set its min size to 1024x768 to prevent text going off screen
window = tk.Tk()
window.minsize(1024,768)
window.title("DMV Warrant Lookup")

#Step 4: Make the function for looking up license plates
def licenseSearch():
    #Step 4.1: Make a temp var for holding in Labels later
    tempVar = entry.get()
    try:
        #Step 4.2: put the database information into variables for easier access later
        licenseOwner = database[tempVar][0]
        warrantsOwner = database[tempVar][1]
        #Step 4.3: make the labels that print  
        nameLabel = tk.Label(window, text="Naperville Trouble Maker: " + licenseOwner)
        nameLabel.pack()
        warrantLabel = tk.Label(window, text="Outstanding Warrants: " + str(warrantsOwner))
        warrantLabel.pack()
        if int(warrantsOwner) > 0:
            warningLabel = tk.Label(window, text="Pull this person over immediately and arrest them!")
            warningLabel.pack()
        elif warrantsOwner == 0:
            niceLabel = tk.Label(window, text="They are ok and have no warrants.")
            niceLabel.pack()
    except:
        failLabel = tk.Label(window, text="Sorry that doesnt exist in the database please enter a valid License Plate")
        failLabel.pack()
        
#Step 5: Make the function that adds the new license plate to the database
def addLicense():
    database[licensePlate.get()] = (name.get(), warrantsNum.get())

#Step 6: Preallocate the entries and button for the newLicense function
licensePlate = tk.Entry(window)
name = tk.Entry(window)
warrantsNum = tk.Entry(window)
addButton = tk.Button(window, text="Add To Database", command=addLicense)

#Step 7: Make the newLicese function
def newLicense():
    #Step 7.1: Prompt the user
    prompt = tk.Label(window, text="Please Type the License Plate, Name, and Warrants in that order")
    prompt.pack()
    #Step 7.2: Pack the previously mentioned entries and button for use in the addLicense function
    licensePlate.pack()
    name.pack()
    warrantsNum.pack()
    addButton.pack()

#Step 8: Create the initial prompts for all the buttons and entries on the screen when you first start the program.
promtSearch = tk.Label(window, text="Type a license plate here to search for it.")
promtSearch.pack()

entry = tk.Entry(window)
entry.pack()

search = tk.Button(window, text ="Search", command=licenseSearch)
search.pack()

promtNewEntry = tk.Label(window, text="Press this button to enter a new License Plate.")
promtNewEntry.pack()

newEntry = tk.Button(window, text="New License Plate", command=newLicense)
newEntry.pack()

#Step 9: create the exit routine as the last button on the main page and have the logic for it.
def exit():
    sys.exit()

exitButton = tk.Button(window, text="Exit", command=exit)
exitButton.pack()

#Step 10: Initialize Main Loop 
window.mainloop()