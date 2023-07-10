with open("Input/Names/invited_names.txt", "r") as names_letter:
    list_name_letter = names_letter.readlines()

with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter = starting_letter.readlines()

first_letter = letter[0].strip()

for name in list_name_letter:
    name_letter = name.strip()
    first_letter_change = first_letter.replace("[name],", f"{name_letter},\n\n")
    with open(f"Output/ReadyToSend/letter_for_{name_letter}.txt", "w") as send:
        send.write(first_letter_change)
        send.write("You are invited to my birthday this Friday.\n\nHope you can make it!\n\nHekal.")
