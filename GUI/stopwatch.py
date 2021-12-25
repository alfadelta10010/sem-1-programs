from tkinter import *

root = Tk()
l1 = Label(root, text="Stopwatch", font=50, fg="blue", bg="grey")
l1.pack()
m = 0
s = 0


def stopwatch():
    global m
    global s
    if s < 59:
        s = s + 1
    elif s == 59:
        s = 0
        m = m + 1
    time = "{0:02d}:{1:02d}".format(m, s)
    l1.config(text=time)  # to update the value of text
    root.after(1000, stopwatch)


stopwatch()
root.mainloop()
