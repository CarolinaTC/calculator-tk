from tkinter import *

root = Tk() # create a gui window

#Define layout of calculator
root.title("calculator")
root.configure(background='light grey')
root.geometry('520x300')
equation = StringVar()
e = Entry(root,textvariable=equation, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=39, pady=10)

def button_press(number):
    #e.delete(0, END) #not sure
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_sum():
    first_number = e.get()
    global f_num
    global math
    math = "sum"
    f_num = int(first_number)
    e.delete(0,END)

def button_sub():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)


def button_div():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def button_mult():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def button_equal():
    second_number = e.get()
    e.delete(0, END)

    if math == "sum":
        e.insert(0, f_num + int(second_number))

    if math == "subtraction":
        e.insert(0, f_num - int(second_number))

    if math == "multiplication":
        e.insert(0, f_num * int(second_number))

    if math == "division":
        e.insert(0, f_num / int(second_number))

#create buttons
button1 = Button(root, text='1', padx=40, pady=20, command=lambda: button_press(1))
button2 = Button(root, text='2', padx=40, pady=20, command=lambda: button_press(2))
button3 = Button(root, text='3', padx=40, pady=20, command=lambda: button_press(3))
button4 = Button(root, text='4', padx=40, pady=20, command=lambda: button_press(4))
button5 = Button(root, text='5', padx=40, pady=20, command=lambda: button_press(5))
button6 = Button(root, text='6', padx=40, pady=20, command=lambda: button_press(6))
button7 = Button(root, text='7', padx=40, pady=20, command=lambda: button_press(7))
button8 = Button(root, text='8', padx=40, pady=20, command=lambda: button_press(8))
button9 = Button(root, text='9', padx=40, pady=20, command=lambda: button_press(9))
button0 = Button(root, text='0', padx=40, pady=20, command=lambda: button_press(0))

button_sum = Button(root, text='+', padx=39, pady=20, command= button_sum)
button_sub = Button(root, text='-', padx=39, pady=20, command= button_sub)
button_div = Button(root, text='/', padx=39, pady=20, command= button_div)
button_mul = Button(root, text='x', padx=39, pady=20, command= button_mult)
button_clear = Button(root, text='clear', padx=30, pady=20, command= button_clear)
button_equal = Button(root, text='=', padx=39, pady=20, command= button_equal)
#button_dot = Button(root, text='clear', padx=40, pady=20, command=button_add)



#put buttons on screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)
button_sub.grid(row=3, column=3)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2 ,column=2)
button_mul.grid(row=2 ,column=3)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)
button_div.grid(row=1, column=3)

button0.grid(row=4, column=0)
button_clear.grid(row=4, column=1)
#button_dot.grid(row=4, column=2)
button_equal.grid(row=4, column=2)
button_sum.grid(row=4, column=3)


root.mainloop()

