import os, os.path
import time
import re
from datetime import datetime
import random

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
    return Date

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
path = "C:\\Users\\TCMUSALICI\\Desktop\\YL\\Python\\Notepad.txt"
TagPath = "C:\\Users\\TCMUSALICI\\Desktop\\YL\\Python\\Tags.txt"
val = int(input("Please enter your choice.\n"))

def AddNote():
    #The field where the NUMBER of the TXT file is specified.
    NoteNumber = random.randint(1,1000)

    #The field where the TITLE of the TXT file is specified.
    NoteTitle = input("Please enter the title of your note's.\n")
    NoteTitle = NoteTitle + ".txt"

    #The field where the CONTEXT of the TXT file is specified.
    NoteComment = input("Please enter the comment for your note's.\n")

    #The field where the TITLE, NOTENUMBER, DATE and NOTETAG of the TXT file is stored.
    NotesTextFile = open(path, "r")
    print(NotesTextFile.read())

    #The field where the TAG of the TXT file is specified.
    NoteTag = input("Please enter the tag of your note's. You can choose one of the available tags or not at all.\n")
    NoteTagNumber = random.randint(1,1000)
    if not NoteTag:
        NewNote = str(NoteTitle) + "," + str(NoteComment) +"," + str(NoteNumber) + "," + str(Date) + ",None" +"\n"
    else:
        NewNote = str(NoteTitle) + "," + str(NoteComment) +"," + str(NoteNumber) + "," + str(Date) + "," + str(NoteTagNumber) + "\n"
    
    File = open(path, "a+")
    File.write(NewNote)
    File.close()

def DeleteNote():
    NotesTextFileRead = open(path, "r")
    print(NotesTextFileRead.read())
    OriginalFile = "C:\\Users\\TCMUSALICI\\Desktop\\YL\\Python\\Notepad.txt"
    TempFile = "C:\\Users\\TCMUSALICI\\Desktop\\YL\\Python\\TempNotepad.txt"
    Del = str(input("Which txt file will be deleted? Please enter file's number!\n"))
    with open(OriginalFile, "r") as input:
        with open(TempFile, "w") as output:
            # iterate all lines from file
            for line in input:
                # if substring contain in a line then don't write it
                if Del not in line.strip("\n"):
                    output.write(line)
    for retry in range(100):
        #access denied problems solved with this for loop
        try:
            # replace file with original name
            os.replace(TempFile, OriginalFile)
            break
        except:
            print ("Replace failed, retrying...")
    
def UpdateNote():
    NotesTextFileRead = open(path, "r")
    print(NotesTextFileRead.read())
    NoteName= input("Which note will be updated?\n")
    NotesTextFileWrite = open(path, "w")
    Update = input("Please update your note.\n")
    with open(r'Notepad.txt', 'r') as file:
        data = file.read()
        data = data.replace(NoteName, Update)
    with open(r'Notepad.txt', 'w') as file:
        file.write(data)

def ListNote():
    File = open(path, "r")
    for Line in File.readlines():
        print(Line)
    File.close()

def AddTag():
    TagNumber = random.randint(1,1000)
    NewTag = input("Please enter new tag.\n")
    File = open("Tags.txt", "a")
    File.write(str(TagNumber)+ "," + NewTag)
    File.close()
    
def DeleteTag():
    File = open(path, "r") #The field where the TAGS shown
    for Line in File.readlines():
        CurrentLine = Line.split(",")
        print(CurrentLine[3])

    File = open(TagPath, "r")
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
    File = open(path, "r")
    for Line in File.readlines():
        CurrentLine = Line.split(",")
        print(CurrentLine[4])
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
