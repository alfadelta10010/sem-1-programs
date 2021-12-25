from tkinter import *

root = Tk()
l1 = Label(root, text="hello", font=20, fg="red", bg="yellow")
e1 = Entry(root, width=50)
e1.insert(0, "Enter a name")
l1.grid(row=0, column=0)
e1.grid(row=1, column=0)


def display():
    name = e1.get()
    if name == "Garima":
        l2 = Label(root, text="Hello {} :), Welcome to PES".format(name))
    else:
        l2 = Label(root, text="Hello {}, Welcome to PES".format(name))
    l2.grid()


b1 = Button(root, text="Click me xD", command=display)
b1.grid(row=5, column=0)
c1 = Checkbutton(root, text="hello", activeforeground="blue")
c1.grid(row=7, column=0)
cc1 = IntVar()

root.mainloop()
