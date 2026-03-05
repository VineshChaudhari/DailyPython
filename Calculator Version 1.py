#Basic Calculator#

print("Enter Number to do calculating operation")
a = float(input("Number 1: "))
b = float(input("Number 2: "))

print("What operation you want to do Adition, Subtraction, Multiplication, Division")
operation = input("Enter operation: ")

Addition = a + b
Subtraction = a-b
Multiplication = a*b
Division = a/b

if operation == "Addition":
    print("Adition is a+b: ",Addition)

elif operation == "Subtraction":
    print("Subtraction is a-b: ", Subtraction)

elif operation == "Multiplication":
    print("Multiplication is a*b: ", Multiplication)

else:
    print("Division is a/b: ", Division)
