from tkinter import *

root = Tk()
def function():
    id = e1.get()
    pas = e2.get()
    print(id, pas)


l1 = Label(root, text="LOGIN PAGE", font=30)
l2 = Label(root, text="Enter ID: ", font=30)
e1 = Entry(root, width=20)
l3 = Label(root, text="Enter Password: ", font=30)
e2 = Entry(root, width=20, show="*")
l1.grid(row=0, column=1)
l2.grid(row=1, column=0)
e1.grid(row=1, column=2)
l3.grid(row=2, column=0)
e2.grid(row=2, column=2)

b1 = Button(root, text="LOGIN", command=function)
b1.grid(row=3, column=1)
root.mainloop()
