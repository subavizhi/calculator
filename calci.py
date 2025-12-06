import math

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def mod(a, b):
    return a % b

def floordiv(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a // b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        return "Error: Square root of negative number not allowed!"
    return math.sqrt(a)

def show_menu():
    print("\n----------------------------")
    print("     📌 ADVANCED CALCI")
    print("----------------------------")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Floor Division (//)")
    print("7. Power (**)")
    print("8. Square Root (√)")
    print("9. Exit")
    print("----------------------------")

while True:
    show_menu()
    choice = input("Choose an option (1-9): ")

    if choice == "9":
        print("\nThanks for using Advanced Calci! Goodbye 😊")
        break

    # Square root takes only one number
    if choice == "8":
        num = float(input("Enter a number: "))
        print("Result:", sqrt(num))
        continue

    # All other operations use two numbers
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if choice == "1":
        print("Result:", add(num1, num2))
    elif choice == "2":
        print("Result:", sub(num1, num2))
    elif choice == "3":
        print("Result:", mul(num1, num2))
    elif choice == "4":
        print("Result:", div(num1, num2))
    elif choice == "5":
        print("Result:", mod(num1, num2))
    elif choice == "6":
        print("Result:", floordiv(num1, num2))
    elif choice == "7":
        print("Result:", power(num1, num2))
    else:
        print("Invalid choice! Please pick between 1–9.")
