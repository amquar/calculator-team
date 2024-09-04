import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.number =""
        self.current_input = ""
        self.result = None
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

        self.button = tk.Button(self.root, text="÷", height=3, width=8)
        self.button.place(x=220, y=80)

        self.button = tk.Button(self.root, text="7", height=3, width=8, command=lambda: self.input_number("7"))
        self.button.place(x=10, y=135)

        self.button = tk.Button(self.root, text="8", height=3, width=8, command=lambda: self.input_number("8"))
        self.button.place(x=80, y=135)

        self.button = tk.Button(self.root, text="9", height=3, width=8, command=lambda: self.input_number("9"))
        self.button.place(x=150, y=135)

        self.button = tk.Button(self.root, text="x", height=3, width=8)
        self.button.place(x=220, y=135)

        self.button = tk.Button(self.root, text="4", height=3, width=8, command=lambda: self.input_number("4"))
        self.button.place(x=10, y=190)

        self.button = tk.Button(self.root, text="5", height=3, width=8, command=lambda: self.input_number("5"))
        self.button.place(x=80, y=190)

        self.button = tk.Button(self.root, text="6", height=3, width=8, command=lambda: self.input_number("6"))
        self.button.place(x=150, y=190)

        self.button = tk.Button(self.root, text="-", height=3, width=8)
        self.button.place(x=220, y=190)

        self.button = tk.Button(self.root, text="1", height=3, width=8, command=lambda: self.input_number("1"))
        self.button.place(x=10, y=245)

        self.button = tk.Button(self.root, text="2", height=3, width=8, command=lambda: self.input_number("2"))
        self.button.place(x=80, y=245)

        self.button = tk.Button(self.root, text="3", height=3, width=8, command=lambda: self.input_number("3"))
        self.button.place(x=150, y=245)

        self.button = tk.Button(self.root, text="+", height=3, width=8)
        self.button.place(x=220, y=245)

        self.button = tk.Button(self.root, text="0", height=3, width=18, command=lambda: self.input_number("0"))
        self.button.place(x=10, y=305)

        self.button = tk.Button(self.root, text=".", height=3, width=8)
        self.button.place(x=150, y=305)

        self.buttonAns = tk.Button(self.root, text="=", height=3, width=8, command=(self))
        self.buttonAns.place(x=220, y=305)

        self.root.mainloop()

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
        if self.current_input != "":
            self.backspace()
            self.clear()
        else:
            self.update_label()
    
    
MyCalculator()