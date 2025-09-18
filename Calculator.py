def calculator():
    print("Welcome to Python Calculator 🧮")
    print("Operations: +, -, *, /, %")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operator (+, -, *, /, %): ")
            num2 = float(input("Enter second number: "))

            if op == "+":
                result = num1 + num2
            elif op == "-":
                result = num1 - num2
            elif op == "*":
                result = num1 * num2
            elif op == "/":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Error! Division by zero."
            elif op == "%":
                result = num1 % num2
            else:
                result = "Invalid Operator!"

            print("Result:", result)

        except ValueError:
            print("Invalid input! Please enter numbers only.")

        # Exit option
        choice = input("Do you want to continue? (yes/no): ").lower()
        if choice == "no":
            print("Exiting Calculator. Goodbye!")
            break

calculator()
