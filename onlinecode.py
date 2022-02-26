from tkinter import *
import turtle
import tkinter.messagebox

root = Tk()

canvas = Canvas(master=root, width=400, height=400)
turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("red")
canvas.grid(padx=5, pady=5, row=0, column=0, rowspan=10, columnspan=10)  # , sticky='nsew')
draw = turtle.RawTurtle(turtle_screen)
draw.penup()
draw.setpos(-175, -175)

def Board(a, x, y, size):
    # draw.pu()
    draw.penup()
    draw.goto(x, y)
    # draw.pd()
    draw.pendown()
    for i in range(0, 4):
        draw.forward(size)
        draw.right(90)


def Board2():
    x = -40
    y = -40
    size = 40
    for i in range(0, 10):
        for j in range(0, 10):
            Board(draw, x + j * size, y + i * size, size)


def Button_click():
    tkinter.messagebox.showinfo("Game", "Tic Tac Toe")


# button = tkinter.Button(window, text = "Play!", command = Button_click)
# button = Tk.Button(window, text = "Play!", command = Button_click)
# button.pack()
#
Play_Button = tkinter.Button(master=root, text="Play!", command=Button_click)
Play_Button.config(bg="cyan", fg="black")
Play_Button.grid(padx=2, pady=2, row=0, column=11, sticky='nsew')

Board_Button = tkinter.Button(master=root, text="Draw_Board", command=Board2)
Board_Button.config(bg="cyan", fg="black")
Board_Button.grid(padx=2, pady=2, row=1, column=11, sticky='nsew')
#
root.mainloop()


