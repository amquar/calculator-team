import tkinter as tk

class MyCalculator:
    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("300x340")
        self.root.title("My Calculator")

        self.label = tk.Label(self.root, text="sum", font=('Montserrat', 18))
        self.label.pack()

        self.button = tk.Button(self.root, text="AC", height=3, width=8)
        self.button.place(x=10, y=50)

        self.button = tk.Button(self.root, text="+/-", height=3, width=8)
        self.button.place(x=80, y=50)

        self.button = tk.Button(self.root, text="⌫", height=3, width=8)
        self.button.place(x=150, y=50)

        self.button = tk.Button(self.root, text="÷", height=3, width=8)
        self.button.place(x=220, y=50)

        self.button = tk.Button(self.root, text="7", height=3, width=8)
        self.button.place(x=10, y=105)

        self.button = tk.Button(self.root, text="8", height=3, width=8)
        self.button.place(x=80, y=105)

        self.button = tk.Button(self.root, text="9", height=3, width=8)
        self.button.place(x=150, y=105)

        self.button = tk.Button(self.root, text="x", height=3, width=8)
        self.button.place(x=220, y=105)

        self.button = tk.Button(self.root, text="4", height=3, width=8)
        self.button.place(x=10, y=160)

        self.button = tk.Button(self.root, text="5", height=3, width=8)
        self.button.place(x=80, y=160)

        self.button = tk.Button(self.root, text="6", height=3, width=8)
        self.button.place(x=150, y=160)

        self.button = tk.Button(self.root, text="-", height=3, width=8)
        self.button.place(x=220, y=160)

        self.button = tk.Button(self.root, text="1", height=3, width=8)
        self.button.place(x=10, y=215)

        self.button = tk.Button(self.root, text="2", height=3, width=8)
        self.button.place(x=80, y=215)

        self.button = tk.Button(self.root, text="3", height=3, width=8)
        self.button.place(x=150, y=215)

        self.button = tk.Button(self.root, text="+", height=3, width=8)
        self.button.place(x=220, y=215)

        self.button = tk.Button(self.root, text="0", height=3, width=18)
        self.button.place(x=10, y=275)

        self.button = tk.Button(self.root, text=".", height=3, width=8)
        self.button.place(x=150, y=275)

        self.buttonAns = tk.Button(self.root, text="=", height=3, width=8, command=(self))
        self.buttonAns.place(x=220, y=275)



        self.root.mainloop()


    def ansFn(self):
        self.label

MyCalculator()