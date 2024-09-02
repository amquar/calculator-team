# Equation function

def calculate_equation(equation):
    try:
        result = eval(equation)
        
        print(f"The result of the equation '{equation}' is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print(f"Error: Invalid equation. {str(e)}")

def calculator():
    print("Welcome to the Equation Calculator")
    print("You can use +, -, *, /, and parentheses in your equation.")
    print("For example: (2 + 3) * 4 / 5")
    
    equation = input("Enter the equation: ")
    
    calculate_equation(equation)

calculator()
