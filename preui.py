import tkinter as tk

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

        self.create_buttons()
        self.root.mainloop()

    def create_buttons(self):
        buttons = [
            ('AC', 10, 80, self.clear),
            ('+/-', 80, 80, None),
            ('⌫', 150, 80, self.backspace),
            ('÷', 220, 80, lambda: self.set_operation('/')),
            ('7', 10, 135, lambda: self.input_number("7")),
            ('8', 80, 135, lambda: self.input_number("8")),
            ('9', 150, 135, lambda: self.input_number("9")),
            ('x', 220, 135, lambda: self.set_operation('*')),
            ('4', 10, 190, lambda: self.input_number("4")),
            ('5', 80, 190, lambda: self.input_number("5")),
            ('6', 150, 190, lambda: self.input_number("6")),
            ('-', 220, 190, lambda: self.set_operation('-')),
            ('1', 10, 245, lambda: self.input_number("1")),
            ('2', 80, 245, lambda: self.input_number("2")),
            ('3', 150, 245, lambda: self.input_number("3")),
            ('+', 220, 245, lambda: self.set_operation('+')),
            ('0', 10, 305, lambda: self.input_number("0"), 18),
            ('.', 150, 305, lambda: self.input_number(".")),
            ('=', 220, 305, self.calculate)
        ]

        for (text, x, y, command, width) in buttons:
            width = width if width else 8
            button = tk.Button(self.root, text=text, height=3, width=width, command=command)
            button.place(x=x, y=y)

    def input_number(self, number):
        self.current_input += number
        self.update_label()

    def backspace(self):
        if self.current_input:
            self.current_input = self.current_input[:-1]
        self.update_label()

    def update_label(self):
        display_text = self.current_input if self.current_input else str(self.result if self.result is not None else "")
        self.label.config(text=display_text)

    def clear(self):
        self.current_input = ""
        self.result = None
        self.operation = None
        self.update_label()

    def set_operation(self, operation):
        if self.current_input:
            if self.result is None:
                self.result = float(self.current_input)
            else:
                self.calculate()
            self.current_input = ""
            self.operation = operation

    def calculate(self):
        if self.current_input and self.operation:
            if self.operation == '+':
                self.result += float(self.current_input)
            elif self.operation == '-':
                self.result -= float(self.current_input)
            elif self.operation == '*':
                self.result *= float(self.current_input)
            elif self.operation == '/':
                try:
                    self.result /= float(self.current_input)
                except ZeroDivisionError:
                    self.result = "Error"
            
            self.current_input = ""
            self.operation = None
            self.update_label()

MyCalculator()
