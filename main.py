
notes = []

options_text = "- Press 1 to add a new note.\n" \
               "- Press 2 to change a note.\n" \
               "- Press 3 to delete a note."


def add_note():
    note = input("Enter a note: ")
    notes.append(note)


def change_note(index):
    notes[index] = input("Enter the new text: ")


def remove_note(index):
    notes.remove(notes[index])


def display_notes():
    for i, note in enumerate(notes):
        print(f'- {i + 1}: {note}')


while True:
    print(options_text)
    selection = int(input("Enter a number >> "))

    if selection == 1:
        add_note()
    elif selection == 2:
        display_notes()
        note_selection = int(input("Which note would you like to edit? ")) - 1
        change_note(note_selection)
    elif selection == 3:
        note_selection = int(input("Which note would you like to remove? ")) - 1
        remove_note(note_selection)

    display_notes()
    print()