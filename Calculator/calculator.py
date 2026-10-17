def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

print("---- WELCOME to CALCULATOR ----")

while True:
    choice = input("Choose Operation: +, -, *, /, **, %, or exit press q: ").strip()
    if choice.lower() == "q":
        print("Comeback whenever you want")
        break
    try:
        number1 = float(input("First Number: "))
        number2 = float(input("Second Number: "))
    except ValueError:
        print("Please enter a valid number!")
        continue
    try:
        if choice == "+":
            result = add(number1, number2)
            
        elif choice == "-":
            result = subtract(number1, number2)

        elif choice == "*":
            result = multiply(number1, number2)

        elif choice == "/":
            result = divide(number1, number2)

        elif choice == "**":
            result = power(number1, number2)

        elif choice == "%":
            result = modulo(number1, number2)

        else:
            print("Invalid Operation! ")
            continue
    except ZeroDivisionError:
        print("Can't divide by zero")
        continue
    print(f"Result: {result}")
    continue


     