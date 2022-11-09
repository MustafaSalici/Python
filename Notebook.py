# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:31:15 2022

@author: MUSALICI
"""

import os, os.path
import time
import re
from datetime import datetime

print('Hello, ' + os.getlogin() + '! How are you?')

def InputDate():
    Date = input("Enter date in the format (DD.MM.YYYY) : ")
    Format = "%d.%m.%Y"
    try:
        res = bool(datetime.strptime(Date, Format))
    except ValueError:
        res = False
    if(res is False):
        print("Please enter in the correct format! >>> (DD.MM.YYYY)")
        InputDate()

Date = InputDate()

text = """
1) Add Note
2) Delete Note
3) Update Note
4) List Note
5) Add Tag
6) Delete Tag
7) List Tag
0) Exit
"""
print(text)

val = int(input("Please enter your choice.\n"))

def AddNote():
    
    #The field where the NUMBER of the TXT file is specified.
    path = "C:\\Users\\MUSTAFASALICI\\Desktop\\YL\\Python"
    NoteNumber = int(len([name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]))

    #The field where the TITLE of the TXT file is specified.
    NoteTitle = input("Please enter the title of your note's.\n")
    NoteTitle = NoteTitle + ".txt"
    NewNote = open(NoteTitle, "a+")

    #The field where the CONTEXT of the TXT file is specified.
    f = open(NoteTitle, "w")
    f.write(input("Please enter the comment for your note's.\n"))
    f.close()
    f = open(NoteTitle, "r")

    #The field where the TITLE, NOTENUMBER, DATE and NOTETAG of the TXT file is stored.
    NotesTextFile = open("Notes.txt", "r")
    print(NotesTextFile.read())

    #The field where the TAG of the TXT file is specified.
    NoteTag = input("Please enter the tag of your note's. You can choose one of the available tags or not at all.\n")
    if not NoteTag:
        TagContents = str(NoteTitle) + "," + str(NoteNumber) + "\n"
    else:
        TagContents = str(NoteTitle) + "," + str(NoteNumber)+ "," +  str(NoteTag) + "\n"
    t = open("Notes.txt", "a+")
    t.writelines(TagContents)
    t.close()

def DeleteNote():
    NotesTextFile = open("Notes.txt", "r")
    print(NotesTextFile.read())
    Del = input("Which txt file will be deleted?\n")
    NotesTextFile = NotesTextFile.readlines()
    os.remove(Del)

def UpdateNote():
    path = "C:\\Users\\MUSTAFASALICI\\Desktop\\YL\\Python"
    dirs = os.listdir(path)
    for note in dirs:
        if note.endswith(".txt"): # Prints only text file present folder
            print(note)
    NoteName= input("Which note will be updated?\n")
    if os.path.exists(NoteName):
        f = open(NoteName, "a+")
        Update = input("Please update your note.\n")
        Update = "\n" + Update
        f.write(Update)
    else:
        print("Note has not exist!")

def ListNote():
    path = "C:\\Users\\MUSTAFASALICI\\Desktop\\YL\\Python"
    dirs = os.listdir(path)
    for note in dirs:
        if note.endswith(".txt"): # Prints only text file present folder
            print(note)

def AddTag():
    print("Hello")
    
def DeleteTag():
    File = open("Notes.txt", "r") #The field where the TAGS shown
    for Line in File.readlines():
        CurrentLine = Line.split(",")
        print(CurrentLine[3])

    File = open("Notes.txt", "r")
    Del = str(input("Which tag will be deleted?\n"))
    for Line in File.readlines():
        print(Line)
        CurrentLine = Line.split(",")
        print(CurrentLine[3])
        if CurrentLine[3] != Del:
            Line.write(CurrentLine)
            print(CurrentLine)
            print(Del + " is deleted!")
    File.close()

def ListTag():
    File = open("Notes.txt", "r")
    for Line in File.readlines():
        CurrentLine = Line.split(",")
        print(CurrentLine[2])
    File.close()

def Exit():
    print("You log out after 5 seconds")
    time.sleep(5)
    quit()

if (val == 1): 
    AddNote()
elif val == 2: 
    DeleteNote()
elif val == 3: 
    UpdateNote()
elif val == 4: 
    ListNote()
elif val == 5: 
    AddTag()
elif val == 6: 
    DeleteTag()
elif val == 7: 
    ListTag()
elif val == 0: 
    Exit()
else: 
    print("Please enter valid number!")
