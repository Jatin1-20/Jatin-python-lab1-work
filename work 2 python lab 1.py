def takeInput():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator (+,-,*,/): ")
    return num1, num2, operator

def displayResult():
    num1, num2, operator = takeInput()

    if operator == "+":
        result = num1 + num2
        formula = f"{num1} + {num2} = {result}"
    elif operator == "-":
        result = num1 - num2
        formula = f"{num1} - {num2} = {result}"
    elif operator == "*":
        result = num1 * num2
        formula = f"{num1} * {num2} = {result}"
    elif operator == "/":
        result = num1 / num2
        formula = f"{num1} / {num2} = {result}"
    else:
        print("Invalid operator entered")
        return

    print(formula)

displayResult()
