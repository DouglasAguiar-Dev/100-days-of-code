# GREETINGS
print("Welcome to the Tip Calculator!")


# INPUT BILL LOOP + VALIDATION
def get_bill():
    while True:
        try:
            value = float(input("What was the total Bill? $"))
            if value <= 0:
                print("Bill must be greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid bill input, Please enter numbers only.")


# INPUT TIP LOOP + VALIDATION
def get_tip():
    while True:
        try:
            value = int(input("What percentage Tip would you like to give? (10, 12, or 15): "))

            if value in [10, 12, 15]:
                return value
            else:
                print("Tips must be 10, 12, or 15.")
        except ValueError:
            print("Invalid tip input, Please enter numbers only.")


# INPUT PEOPLE LOOP + VALIDATION
def get_people():
    while True:
        try:
            value = int(input("How many people to split the Bill? "))
            if value <= 0:
                print("People must be greater than 0.")
            else:
                return value
        except ValueError:
            print("Invalid people input, Please enter numbers only.")


# FUNCTION CALLS
bill = get_bill()
tip = get_tip()
people = get_people()

# CALCULATIONS
bill_total = bill + (bill * (tip / 100))
total_per_person = bill_total / people
total_without_tips = bill / people

# OUTPUT
print(f"Bill per person (With Tips): ${total_per_person:.2f}")
print(f"Bill per person (Without Tips): ${total_without_tips:.2f}")
