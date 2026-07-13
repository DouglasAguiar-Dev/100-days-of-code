print("Welcome to Band Name Generator by Douglas Aguiar")

while True:
    # Handle input city
    while True:
        city_name = input("What is your favorite city name?\n").strip().title()
        if city_name == "":
            print("Oops! You forgot to type your city name.")
            continue 
        break
            
    # Handle input pet   
    while True: 
        pet_name = input("Now enter your pet's name:\n").strip().title()
        if pet_name == "":
            print("Oops! You forgot to type your pet's name.")
            continue 
        break
            
    # print names
    print(f"The name of your Band could be: {city_name} {pet_name}")
        
    # Restart or exit the program 
    while True:
        should_continue = input("Type 'r' to retry a new name or 'n' to exit the program:\n").strip().lower()
        if should_continue == 'n':
            print("bye!")
            exit()  # Using exit() here to completely stop the program 
        elif should_continue == 'r':
            break # Escapes this mini-loop, allowing the master loop to restart
        else: 
            print("Invalid input, Try again.")
