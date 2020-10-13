from tkinter import Tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("My Amazing calculator-tkinter")

root = Tk()
calculator = Calculator(root)
root.mainloop()
