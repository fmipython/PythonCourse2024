import json

def list():
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

    print("Listing notes...")
    if len(notes) == 0:
        print("Nothing to list.")
    else:
        for title in notes:
            print("- " + title + " (Due: " + (notes[title]["due_date"] if notes[title]["due_date"] else "None") + ")")
