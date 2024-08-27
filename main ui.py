import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.number =""
        self.root = tk.Tk()

        self.root.geometry("300x370")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="", font=('Montserrat', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="AC", height=3, width=8)
        self.button.place(x=10, y=80)

        self.button = tk.Button(self.root, text="+/-", height=3, width=8)
        self.button.place(x=80, y=80)

        self.button = tk.Button(self.root, text="⌫", height=3, width=8)
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

        self.button = tk.Label(text="test")
        self.button.place(x=10,y=20)
        
        self.root.mainloop()


    def ansFn(self):
        self.label
        
    def input_number(self, number):
        self.number = number
        

        print(self.number)

        
MyCalculator()