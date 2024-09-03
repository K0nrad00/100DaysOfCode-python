# Demo: https://appbrewery.github.io/python-day10-demo/
# from art import logo # Not importing logo
# print(logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}

# print(operations)
# TODO: Use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary.
# print(operations["*"](4,8))

def list_operations(dictionary):
    for key in dictionary:
        print(key)

# calculate the result of the selected operations
def calculation(number1, number2):
    for key in operations:
        return operations[select_operation](number1, number2)

def format_result(number1, number2, calculation_result):
    return f"{number1} {select_operation} {number2} = {str(calculation_result)}"


first_number = float(input("Provide the first number: \n"))

continue_with_result = True

while continue_with_result:
    list_operations(operations)
    select_operation = input("Provide operations from the choices: ")
    second_number = float(input("Provide the second number: \n"))
    result = calculation(first_number, second_number)
    print("Result:", format_result(first_number, second_number, result))
    continue_with_result = input(f"Would you like to continue working with the {result} result? type 'y' or 'n'")
    if continue_with_result == "n":
        print("\n" * 20)
        first_number = float(input("Provide the first number: \n"))
    else:
        first_number = result
