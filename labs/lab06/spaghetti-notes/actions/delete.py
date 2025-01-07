import json

def delete(title):
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
        print("Doesn't exist, can't delete.")
    else:
        del notes[title]
        with open("notes.json", "w") as f:
            json.dump(notes, f)
        print("Deleted.")