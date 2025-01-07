import json


def add(title, content, due_date):
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
            print("No title, can't add note.")
    elif content == "":
        print("No content, can't add note.")
    else:
        if title in notes:
            print("Already exists, won't overwrite.")
        else:
            if due_date:
                notes[title] = {
                    "content": content,
                    "due_date": due_date
                }
            else:
                notes[title] = {
                    "content": content,
                }
            with open("notes.json", "w") as f:
                f.write(json.dumps(notes))
            print("Added new note", title)