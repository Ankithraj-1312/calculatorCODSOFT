def calculator():
    print("Simple Calculator")
    while True:
        num1_input = input("Enter first number or type 'exit': ")
        if num1_input.lower() == 'exit':
            print("thank you!")
            break
        if not num1_input.replace('.', '', 1).isdigit():
            print("enter only number!")
            continue

        num2_input = input("Enter second number or type 'exit': ")
        if num2_input.lower() == 'exit':
            print("thank you!")
            break
        if not num2_input.replace('.', '', 1).isdigit():
            print("enter only number!")
            continue

        num1 = int(num1_input)
        num2 = int(num2_input)

        op = input("Enter operation (+, -, *, /): ")

        if op == "+":
            print("Result:", num1 + num2)
        elif op == "-":
            print("Result:", num1 - num2)
        elif op == "*":
            print("Result:", num1 * num2)
        elif op == "/":
            if num2 != 0:
                print("Result:", num1 // num2)
            else:
                print("Error: Division by zero")
        else:
            print("Invalid operation")


calculator()
