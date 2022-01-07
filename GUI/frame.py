'''
from tkinter import *
root = Tk()
frame1 = Frame(root)
frame2 = Frame(root)
frame3 = Frame(root)
for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0)
l1=Label(frame1, text="Label 1", bg="red", sticky="E")
l2=Label(frame2, text="Label 2", bg="green", sticky="E")
l3=Label(frame3, text="Label 3", bg="blue", sticky="E")
l1.grid()
l2.grid()
l3.grid()
b1=Button(frame1, text="CLICK")
b2=Button(frame2, text="CLICK")
b3=Button(frame3, text="CLICK")
b1.grid()
b2.grid()
b3.grid()

'''
from tkinter import *
root = Tk()

scroll = Scrollbar(root)
# scrollbar function has a function named set, it connects scrollbar to other widgets
# xscrollcommand too
lis1 = Listbox(root, yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
for i in range(1, 100):
    lis1.insert(END, i)
lis1.pack(side=LEFT, fill=Y, expand=1)
scroll.config(command=lis1.yview) 
root.mainloop()


# take a paragraph and scroll it
