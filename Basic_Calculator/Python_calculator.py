# define the functions needed: add, subtract, mutliply, divison etc.
# print options to the user 
# ask for values 
# call the functions

def add(a,b):
    answer = a+b
    print(answer)
    

def subtract(a,b):
    result = 0
    
    if a>b:
        result = a-b
        
    else:
        result = b-a
    
    print(result)  
    
def multiply(a,b):
    result = a*b
    print(result)
    
def divison(a,b):
    result = 0
    if a>b:
        result = a/b
    else:
        result = b/a
        
    print(result)

while True:
    
    print("A - Addition")
    print("B - Subtraction")
    print("C - Multiplication")
    print("D - Divison")
    print("E - Exit")

    choice = input("Kindly make your choice : ")

    if choice == "a" or choice == "A":
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        add(a,b)
        
    elif choice == "b" or choice == "B":
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        subtract(a,b)

    elif choice == "c" or choice == "C":
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        multiply(a,b)

    elif choice == "d" or choice == "D":
        a = int(input("Enter the first number : "))
        b = int(input("Enter the second number : "))
        divison(a,b)

    elif choice == "e" or choice == "E":
        print("Program ended Successfully!!")
        quit()
    

    

        
    
        