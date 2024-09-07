import tkinter as tk

from division import divide_numbers
from minus import minus_numbers
from multiply import multiply_numbers
from plus import plus_numbers

class MyCalculator:
    def __init__(self):

        self.left_operand = ""
        self.right_operand = ""
        self.operator = ""
        self.inputing_right = False
        self.root = tk.Tk()

        self.root.geometry("300x370")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="", font=('Montserrat', 18), anchor='e', bg="white", height=2)
        self.label.pack(fill=tk.BOTH, padx=10, pady=10)

        self.button = tk.Button(self.root, text="AC", height=3, width=8, command=self.clear)
        self.button.place(x=10, y=80)

        self.button = tk.Button(self.root, text="+/-", height=3, width=8)
        self.button.place(x=80, y=80)

        self.button = tk.Button(self.root, text="⌫", height=3, width=8, command=self.backspace)
        self.button.place(x=150, y=80)

        self.button = tk.Button(self.root, text="÷", height=3, width=8, command=lambda: self.call_operator("÷"))
        self.button.place(x=220, y=80)

        self.button = tk.Button(self.root, text="7", height=3, width=8, command=lambda: self.input_number("7"))
        self.button.place(x=10, y=135)

        self.button = tk.Button(self.root, text="8", height=3, width=8, command=lambda: self.input_number("8"))
        self.button.place(x=80, y=135)

        self.button = tk.Button(self.root, text="9", height=3, width=8, command=lambda: self.input_number("9"))
        self.button.place(x=150, y=135)

        self.button = tk.Button(self.root, text="x", height=3, width=8, command=lambda: self.call_operator("x"))
        self.button.place(x=220, y=135)

        self.button = tk.Button(self.root, text="4", height=3, width=8, command=lambda: self.input_number("4"))
        self.button.place(x=10, y=190)

        self.button = tk.Button(self.root, text="5", height=3, width=8, command=lambda: self.input_number("5"))
        self.button.place(x=80, y=190)

        self.button = tk.Button(self.root, text="6", height=3, width=8, command=lambda: self.input_number("6"))
        self.button.place(x=150, y=190)

        self.button = tk.Button(self.root, text="-", height=3, width=8, command=lambda: self.call_operator("-"))
        self.button.place(x=220, y=190)

        self.button = tk.Button(self.root, text="1", height=3, width=8, command=lambda: self.input_number("1"))
        self.button.place(x=10, y=245)

        self.button = tk.Button(self.root, text="2", height=3, width=8, command=lambda: self.input_number("2"))
        self.button.place(x=80, y=245)

        self.button = tk.Button(self.root, text="3", height=3, width=8, command=lambda: self.input_number("3"))
        self.button.place(x=150, y=245)

        self.button = tk.Button(self.root, text="+", height=3, width=8, command=lambda: self.call_operator("+"))
        self.button.place(x=220, y=245)

        self.button = tk.Button(self.root, text="0", height=3, width=18, command=lambda: self.input_number("0"))
        self.button.place(x=10, y=305)

        self.button = tk.Button(self.root, text=".", height=3, width=8)
        self.button.place(x=150, y=305)

        self.buttonAns = tk.Button(self.root, text="=", height=3, width=8, command=self.equal)
        self.buttonAns.place(x=220, y=305)

        self.root.mainloop()

    def equal(self):
        left_operand = ""
        if self.operator == "÷":
            left_operand = divide_numbers(float(self.left_operand), float(self.right_operand))
        elif self.operator == "x":
            left_operand = multiply_numbers(float(self.left_operand), float(self.right_operand))
        elif self.operator == "+":
            left_operand = plus_numbers(float(self.left_operand), float(self.right_operand))
        elif self.operator == "-":
            left_operand = minus_numbers(float(self.left_operand), float(self.right_operand))
        print(left_operand)
        self.left_operand = str(left_operand) if left_operand else ""
        self.right_operand = ""
        self.operator = ""
        self.inputing_right = False
        self.update_label()

    def call_operator(self, operator):
        self.inputing_right = True
        self.operator = operator
        
    def input_number(self, number):
        if self.inputing_right:
            self.right_operand += number
        else:
            self.left_operand += number
        self.update_label()

    def backspace(self):
        if self.inputing_right:
            if self.right_operand:
                self.right_operand = self.right_operand[:-1]
        else:
            if self.left_operand:
                self.left_operand = self.left_operand[:-1]
        self.update_label()
    
    def update_label(self):
        if self.inputing_right:
            display_text = self.right_operand
        else:
            display_text = self.left_operand
        
        self.label.config(text=display_text)

    def clear(self):
        if self.left_operand != "":
            self.backspace()
            self.clear()
        else:
            self.update_label()
    
MyCalculator()