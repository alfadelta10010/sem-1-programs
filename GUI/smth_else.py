from tkinter import *
from tkinter import messagebox

root = Tk()
rr1 = IntVar()
r1 = Radiobutton(root, text="Python", value=1, variable=rr1)
r2 = Radiobutton(root, text="Java", value=2, variable=rr1)
c1 = Canvas(root, width=250, height=200, bg="blue")


def show():
    messagebox.showinfo("Information", "My first message box")


b1 = Button(root, text="Popup", command=lambda: show())
# r1.pack()
# r2.pack()
# c1.pack()
c1.create_rectangle(50, 150, 150, 50, fill="black")
b1.pack()
root.mainloop()
