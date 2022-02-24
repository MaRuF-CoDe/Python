from tokenize import Double
from art import logo

#calculation
#Add
def add(n1,n2):
    return n1 + n2

#substraction
def sub(n1,n2):
    return n1 - n2

#Multiplication
def mul(n1,n2):
    return n1 * n2

#Division
def div(n1,n2):
    return n1 / n2

operations = {
    '+' : add,
    '-' : sub,
    '*' : mul,
    '/' : div
}
def calculation():
    print(logo)
    num1 = float(input("What's the first number?: "))

    should_go = True

    while should_go :
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What's the next number?: "))

        calculation_function = operations[operation_symbol]

        answer = calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"to more calculation with {answer} type y or to start new type n :")=='y':
            num1 = answer
        else:
            should_go = False
            calculation()

calculation()