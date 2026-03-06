a = float(input("Enter any number: "))
b = float(input("Enter any number: "))

if a > b:
    print(a,"is greater in value than",b)
    print("Still inside if block")

else:
    print(b,"is greater in value than",a)
    print("Inside if block")
    
print("Outside if block")
