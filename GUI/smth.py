from tkinter import *

root = Tk()


def click(num):
    current = e1.get()
    e1.delete(0, END)
    e1.insert(0, str(current) + str(num))


def add():
    f_n = e1.get()
    global f_num
    global math
    math = "addition"
    f_num = f_n
    e1.delete(0, END)


def equal():
    s_num = e1.get()
    e1.delete(0, END)
    if math == "addition":
        e1.insert(0, int(f_num) + int(s_num))


def clear():
    e1.delete(0, END)


e1 = Entry(root, width=10, justify=CENTER)
e1.grid(row=0, column=0)
b1 = Button(root, text="1", command=lambda: click(1)).grid(row=1, column=0)
b2 = Button(root, text="2", command=lambda: click(2)).grid(row=1, column=1)
b3 = Button(root, text="3", command=lambda: click(3)).grid(row=1, column=2)
b4 = Button(root, text="4", command=lambda: click(4)).grid(row=2, column=0)
b5 = Button(root, text="5", command=lambda: click(5)).grid(row=2, column=1)
b6 = Button(root, text="6", command=lambda: click(6)).grid(row=2, column=2)
b7 = Button(root, text="7", command=lambda: click(7)).grid(row=3, column=0)
b8 = Button(root, text="8", command=lambda: click(8)).grid(row=3, column=1)
b9 = Button(root, text="9", command=lambda: click(9)).grid(row=3, column=2)
b0 = Button(root, text="0", command=lambda: click(0)).grid(row=1, column=0)
