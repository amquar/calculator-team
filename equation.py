# Equation function

class Equation:
    def calculate_equation(equation):
        try:
              result = eval(equation)
              print(result)
              
        except ZeroDivisionError:
              print("Error: Division by zero is not allowed.")
        except Exception as e:
              print(f"Error: Invalid equation. {str(e)}")

    def __init__(self):
         self.current_input = ""
         self.result = None
         
    def update_label(self):
        display_text = self.current_input if self.current_input else str(self.result if self.result is not None else "")
        self.label.config(text=display_text)

Equation()
