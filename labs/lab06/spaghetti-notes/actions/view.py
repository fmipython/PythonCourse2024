import json

def view(title):
    notes = None
    import os

    if os.path.exists("notes.json"):
        with open("notes.json", "r") as f:
            try:
                notes = json.load(f)
            except:
                notes = {}
    else:
        notes = {}

    if title == "":
        print("Need title.")
    elif title not in notes:
        print("Doesn't exist.")
    else:
        print(title)
        print("---")
        print(notes[title]["content"])
        print("---")
        if notes[title]["due_date"]:
            print("Due:" + notes[title]["due_date"])
        else:
            print("No due date.")