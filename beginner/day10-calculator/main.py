from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

functions = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculation():
    print(logo)
    first_number = float(input("Enter the first number: "))
    keep_calculating = True

    while keep_calculating:

        chosen_symbol = input("Enter a function +, -, * or /: ")
        second_number = float(input("Enter the second number: "))

        function_to_run = functions[chosen_symbol]
        total = function_to_run(first_number, second_number)

        print(f"{first_number} {chosen_symbol} {second_number} = {total}")

        answer = input(f"Type 'y' to continue calculating with {total}, or type 'n' to start a new calculation: ").lower()
        if answer == "y":
            first_number = total
        else:
            keep_calculating = False
            print("\n" * 20)
            calculation()

calculation()
