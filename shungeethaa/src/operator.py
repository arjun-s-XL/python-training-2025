a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
if b != 0:
    print("Division:", a / b)
    print("Modulus:", a % b)
    print("Floor Division:", a // b)
else:
    print("Division, Modulus, and Floor Division not possible")

