from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    if n1 > n2:
        return n1 - n2
    else:
        return n2 - n1
    
def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/": divide}

# num1 = input("What's the first number? ")
# num2 = input("What's the second number? ")

# for symbol in operations:
#     print(symbol, end='  ')
# operation_symbol = input("\nPick an operation from the line above: ")

# calculation_function = operations[operation_symbol]
# answer = calculation_function(int(num1), int(num2))

# print(f"{num1} {operation_symbol} {num2} = {answer}")

def Calculator():
    print(logo)
    cont = True
    num1 = input("What's the first number? ")

    while cont:
        for symbol in operations:
           print(symbol, end='  ')
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = input("What's the next number? ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(int(num1), int(num2))
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        choice = input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation: ").lower()
        
        if choice == 'y':
            num1 = answer
                   
        else:
            cont = False
            print("\n"*15)
            Calculator()
    
            
            
Calculator()
            
    
        