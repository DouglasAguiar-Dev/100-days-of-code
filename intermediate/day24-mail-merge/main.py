with open("intermediate/day24-mail-merge/Input/Letters/starting_letter.txt", mode="r") as letter:
    letter_file = letter.read()

with open("intermediate/day24-mail-merge/Input/Names/invited_names.txt", mode="r") as invite_letter:
    names = (invite_letter.readlines())

for name in names:
    clean_name = name.strip()
    new_letter = letter_file.replace("[name]", clean_name)
    with open(f"intermediate/day24-mail-merge/Output/ReadyToSend/letter_for_{clean_name}.txt", mode="w") as completed_letter:
        completed_letter.write(new_letter)