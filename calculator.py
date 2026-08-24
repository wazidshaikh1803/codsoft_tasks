# Simple Calculator
while True:
    # Get two numbers from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Show operation choices
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    # Perform calculation based on choice
    if choice == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")

    elif choice == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")

    elif choice == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")

    elif choice == '4':
        if num2 == 0:
            print("Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

    else:
        print("Invalid choice! Please select 1, 2, 3, or 4.")

    # Ask if user wants to continue
    again = input("Do you want to continue? (Y/N): ")

    if again.lower() in ['y', 'yes']:
        continue  # go back to the start of the loop for new numbers
    else:
        print("Goodbye!")
        break