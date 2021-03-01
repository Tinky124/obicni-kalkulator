import os

""" Vrlo jednostavna skripta u pythonu """

colors = {
    "yellow": "\033[1;33;33m",
    "green": "\033[1;32;32m",
    "red": "\033[1;31;31m",
    "blue": "\033[1;34;34m",


    "end": "\033[0m"
}

def color(color, string):
    return colors[color] + string + colors["end"]

def addition(first, second):
    return first + second

def subtraction(first, second):
    return first - second

def multiplication(first, second):
    return first * second

def division(first, second):
    return first / second

def modular(first, second):
    return first % second

def intDivision(first, second):
    return first // second

def exponent(first, second):
    return first ** second

choice = None
options = [
    # wtf? must have strings as keys?
    {"name": "Addition", "sign": "+", "func": addition},
    {"name": "Subtraction", "sign": "-", "func": subtraction},
    {"name": "Multiplication", "sign": "*", "func": multiplication},
    {"name": "Division", "sign": "/", "func": division},
    {"name": "Modular Rest", "sign": "%", "func": modular},
    {"name": "Floor Division", "sign": "//", "func": intDivision},
    {"name": "Exponentiation", "sign": "**", "func": exponent},
    # dunno what its called in english. lmao ._.
]

latestResults = []


clearCommand = "cls" if os.sys.platform.__contains__("win") else "clear"


def clear():
    os.system(clearCommand)
    

def requestChoice():
    clear()
    print(color("yellow", "Welcome to this simple calculator, select an option.\n"))

    # is latestResults populated?
    if len(latestResults) > 0:
        print(f"Latest Calculations | Sorted by oldest")
        # print all the cached calculations
        for i in range(0, len(latestResults)):
            print("- " + color("blue", latestResults[i]))

        print("_____________\n")

    for i in range(0, len(options)):
        # list all the options from the options list
        print(f"{i+1}: {options[i]['name']}")


    choice = int(input("> ")) - 1


    if choice >= 0 and choice < len(options):
        clear()
        print(color("yellow", f"Welcome to {options[choice]['name']}!") + ", I accept floats.\n")

        first = float(input("First number:\n> "))
        if first.is_integer():
            first = int(first)

        second = float(input("\nSecond number:\n> "))
        if second.is_integer():
            second = int(second)

        result = options[choice]["func"](first, second)

        print(color('green', f"\nResult: {result}"))
        latestResults.append(f"{first} {options[choice]['sign']} {second} = {result}")

        input(f"Press {color('red', 'enter')} to {color('red', 'go back')}.\n")
        requestChoice()
    else:
        requestChoice()


requestChoice()