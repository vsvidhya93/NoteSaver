from Functions import Add_Notes, View_Notes
import os
print("Welcome to Note Saver!\n")
while True:
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("1.Add a new note")
    print("2.View all notes")
    print("3.Exit\n")
    choice=int(input("Enter your choice: "))
    if choice==1:
        note=input("Enter your note: ")
        Add_Notes(note)
        print("Note saved successfully!")
        print("-------------------------------------------------------")

    elif choice==2:
        print("------Saved Notes------")
        View_Notes()
        print("-------------------------------------------------------")

    elif choice==3:
        print("Goodbye!")
        break
    else:
        print("Not a valid choice.Please try again")


import shutil
os.path.join('C:\\Users\\vsvid\\PycharmProjects\\NoteSaver','.idea')
