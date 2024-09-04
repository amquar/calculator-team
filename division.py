
def divide_numbers():
    try:
        
        num1 = float(input())
        num2 = float(input())
        
        result = num1 / num2
        
        return result
        
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Please enter valid numbers.")

if __name__ == "__main__":
    divide_numbers()
