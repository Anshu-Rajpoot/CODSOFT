# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Options:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")

    user_input = input("Please enter your choice (1/2/3/4/5): ")

    if user_input == "5":
        break
    elif user_input in ("1", "2", "3", "4"):
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if user_input == "1":
            print("Result:", add(num1, num2))
        elif user_input == "2":
            print("Result:", subtract(num1, num2))
        elif user_input == "3":
            print("Result:", multiply(num1, num2))
        elif user_input == "4":
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print("Result:", result)
    else:
        print("Invalid input")
