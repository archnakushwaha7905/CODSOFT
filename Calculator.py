# Simple calculator program in python
print("\n Welcome to the simple calculator!")

while True:

# Display the menu options 
# The calculator will perform basic operations like addition, subtraction, multiplication and division
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    # Enter any two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Ask user to choose an operation
    choice = input("choose an operation (a/b/c/d/e): ")

    # If user selects the option 1
    if choice == 'a':
        result = num1 + num2
        print("The result of addition is: ", result)

    # If user selects the option 2
    elif choice == 'b':
        result = num1 - num2
        print("The result of subtraction is: ", result)

    # If user selects the option 3
    elif choice == 'c':
        result = num1 * num2
        print("The result of multiplication is: ", result)

    # If user selects the option 4
    elif choice == 'd':
        if num2 != 0:
            result = num1 / num2
            print("The result of division is: ", result)
        else:
            print("Error: Division by zero is not allowed.")
    elif choice == 'e':
             print("Exiting the calculator. Goodbye!")
             break

        # If user selects an invalid option
else:
        print("Invalid operation selected.")
