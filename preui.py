import tkinter as tk
from division import divide_numbers  # Assuming this is a custom function for division

class MyCalculator:
    def __init__(self):
        self.current_input = ""
        self.result = None
        self.operation = None
        self.root = tk.Tk()

        self.root.geometry("300x370")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="", font=('Montserrat', 18), anchor='e', bg="white", height=2)
        self.label.pack(fill=tk.BOTH, padx=10, pady=10)

        # Defining buttons
        tk.Button(self.root, text="AC", height=3, width=8, command=self.clear).place(x=10, y=80)
        tk.Button(self.root, text="+/-", height=3, width=8, command=self.toggle_sign).place(x=80, y=80)
        tk.Button(self.root, text="⌫", height=3, width=8, command=self.backspace).place(x=150, y=80)
        tk.Button(self.root, text="÷", height=3, width=8, command=lambda: self.set_operation("÷")).place(x=220, y=80)
        tk.Button(self.root, text="7", height=3, width=8, command=lambda: self.input_number("7")).place(x=10, y=135)
        tk.Button(self.root, text="8", height=3, width=8, command=lambda: self.input_number("8")).place(x=80, y=135)
        tk.Button(self.root, text="9", height=3, width=8, command=lambda: self.input_number("9")).place(x=150, y=135)
        tk.Button(self.root, text="x", height=3, width=8, command=lambda: self.set_operation("x")).place(x=220, y=135)
        tk.Button(self.root, text="4", height=3, width=8, command=lambda: self.input_number("4")).place(x=10, y=190)
        tk.Button(self.root, text="5", height=3, width=8, command=lambda: self.input_number("5")).place(x=80, y=190)
        tk.Button(self.root, text="6", height=3, width=8, command=lambda: self.input_number("6")).place(x=150, y=190)
        tk.Button(self.root, text="-", height=3, width=8, command=lambda: self.set_operation("-")).place(x=220, y=190)
        tk.Button(self.root, text="1", height=3, width=8, command=lambda: self.input_number("1")).place(x=10, y=245)
        tk.Button(self.root, text="2", height=3, width=8, command=lambda: self.input_number("2")).place(x=80, y=245)
        tk.Button(self.root, text="3", height=3, width=8, command=lambda: self.input_number("3")).place(x=150, y=245)
        tk.Button(self.root, text="+", height=3, width=8, command=lambda: self.set_operation("+")).place(x=220, y=245)
        tk.Button(self.root, text="0", height=3, width=18, command=lambda: self.input_number("0")).place(x=10, y=305)
        tk.Button(self.root, text=".", height=3, width=8).place(x=150, y=305)
        tk.Button(self.root, text="=", height=3, width=8, command=self.calculate).place(x=220, y=305)

        self.root.mainloop()

    def input_number(self, number):
        self.current_input += number
        self.update_label()

    def set_operation(self, operation):
        if self.current_input:
            if self.result is None:
                self.result = float(self.current_input)
            else:
                self.calculate()  # calculate the previous operation

            self.current_input = ""
            self.operation = operation
            self.update_label()

    def calculate(self):
        if self.current_input and self.operation:
            if self.operation == "+":
                self.result += float(self.current_input)
            elif self.operation == "-":
                self.result -= float(self.current_input)
            elif self.operation == "x":
                self.result *= float(self.current_input)
            elif self.operation == "÷":
                self.result = divide_numbers(self.result, float(self.current_input))  # Assuming divide_numbers handles division by zero

            self.current_input = ""
            self.operation = None
            self.update_label()

    def toggle_sign(self):
        if self.current_input:
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]  # Remove the negative sign
            else:
                self.current_input = '-' + self.current_input  # Add the negative sign
            self.update_label()

    def backspace(self):
        if self.current_input:
            self.current_input = self.current_input[:-1]
        self.update_label()

    def clear(self):
        self.current_input = ""
        self.result = None
        self.operation = None
        self.update_label()

    def update_label(self):
        display_text = self.current_input if self.current_input else str(self.result if self.result is not None else "")
        self.label.config(text=display_text)

MyCalculator()
