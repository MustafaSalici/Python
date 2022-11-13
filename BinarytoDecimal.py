Binary = input("Enter your binary number: ")
try:
    Decimal = int(Binary,2)  
    print("Decimal equivalent of the entered number :", Decimal)
except ValueError:
    print("Invalid value")