import datetime

def Add_Notes(Notes):
        with open("Notes.txt","a") as note_file:
             note_file.write(f"[{datetime.datetime.now()}] {Notes}\n")


def View_Notes():
    with open("Notes.txt","r") as note_file:
        for note in note_file:
            print(note.strip())




