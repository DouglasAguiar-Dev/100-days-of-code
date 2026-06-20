print("Welcome to Band Name Generator by Douglas Aguiar")

city_name = ""
while city_name == "":
    print("Oops! You forgot to type your city name.")
    city_name = input("What is your favorite city name?\n").strip()
city_title = city_name.title()

pet_name = ""
while pet_name == "":
    print("Oops! You forgot to type your pet's name.")
    pet_name = input("Now enter your pet's name:\n").strip()
pet_title = pet_name.title()

print("The name of your Band could be:",city_title + " " + pet_title)



