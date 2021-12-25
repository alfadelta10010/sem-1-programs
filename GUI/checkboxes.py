from tkinter import *
root = Tk()


def show():
    l1.config(text=cc1.get())
    l2.config(text=cc2.get())
    l3.config(text=cc3.get())


cc1 = StringVar()
cc2 = IntVar()
cc3 = IntVar()

l1 = Label(root, text="CHECKBOX 1 STATUS")
l1.pack()

l2 = Label(root, text="CHECKBOX 2 STATUS")
l2.pack()

l3 = Label(root, text="CHECKBOX 3 STATUS")
l3.pack()

