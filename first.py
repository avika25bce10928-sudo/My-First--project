# Program to build a simple calculator using dictionary

# Addition of 2 numbers
def add( a , b):
    return a + b
    
# Subtraction of 2 numbers
def subtract(a , b):
    return a - b
    
# Multiplication of 2 numbers
def product(a , b):
    return a * b

# Division of 2 numbers
def division(a , b):
    if b == 0:
        return "Error! Division by zero"
    return a / b
    
# Using dictionary mappings
operations = {
    '1': add,
    '2': subtract,
    '3': product,
    '4': division, 
}

    
# User Menu
print('Select operation of ur choice')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. Division')

choice = input("Enter operation from the choices (1-4):")

if choice in operations:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
else:
    print("Choice is not in the given list")
    exit()
    
# Function calling
result = operations[choice](n1 ,n2)
print('Results : \n', result)
    