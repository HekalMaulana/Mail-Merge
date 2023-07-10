PLACEHOLDER = "[name]"

with open("Input/Names/invited_names.txt", "r") as names_letter:
    list_name_letter = names_letter.readlines()

with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter = starting_letter.read()
    for name in list_name_letter:
        name_letter = name.strip()
        new_letter = letter.replace(PLACEHOLDER, name_letter)
        with open(f"Output/ReadyToSend/letter_for_{name_letter}.txt", "w") as send:
            send.write(new_letter)
