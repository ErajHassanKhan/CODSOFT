def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("///////////////////Simple Calculator//////////////////// ")
    print("*******operations*********")
    print("Enter 'a' for addition")
    print("Enter 's' for subtraction")
    print("Enter 'm' for multiplication")
    print("Enter 'd' for division")
    print("Enter 'q' to end the program")

    user_input = input("")

    if user_input == "q":
        break

    if user_input in ("a", "s", "m", "d"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "a":
            print("Result: {:.2f}".format(add(num1, num2)))
        elif user_input == "s":
            print("Result: {:.2f}".format(subtract(num1, num2)))
        elif user_input == "m":
            print("Result: {:.2f}".format(multiply(num1, num2)))
        elif user_input == "de":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result: {:.2f}".format(result))
        else:
            print("Invalid input")
    else:
        print("Invalid input")
