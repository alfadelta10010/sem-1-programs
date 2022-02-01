# One player thinks of a word, phrase or sentence and the other tries to guess it
# by suggesting letters within a certain number of guesses.  If the guessing player
# suggests a letter which occurs in the word, the other player writes it in all its
# correct positions. If the suggested letter does not occur in the word, the other
# player draws one element of a hanged stick figure as a tally mark.

import random
import time
import turtle
import os
from tkinter import *

root = Tk()

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=9)
root.columnconfigure(1, weight=8)
root.title('Hangman')

guess = ""
oldGuess = ""

def clearScreen():
    if os.name in ('nt', 'dos'):
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)
    turtle_screen.clear()
    turtle_screen.bgcolor("#346B31")
    draw.setpos(-125, -125)
    draw.color("#FBF7F5")
    draw.speed(1)


def clearFrame(frame):
    for widget in frame.winfo_children():
        widget.destroy()


def getInput(f):
    answerIn1 = f.get()
    return answerIn1


def answerInput(inp):
    global guess, oldGuess
    oldGuess = guess
    guess = inp.get()


def mainGame(answerIn, mode):
    clearFrame(frame2)
    print(answerIn)
    vowelsList = ["a", "e", "i", "o", "u"]
    L = [face, leg, body, hands, head, stand]
    answer = list(answerIn)
    display = []
    display.extend(answer)  # Will contain the word in list form
    for i in range(len(display)):
        w = 0
        for j in range(len(vowelsList)):
            if display[i] == vowelsList[j]:
                w = 1
        if w == 0:
            display[i] = "_"
    disp = " ".join(display)  # Contains the word in list form with blanks
    print(disp)
    print()

    h5 = Label(frame2, text="————————————————\n GUESS THE WORD \n————————————————", bg="#85491b", bd=3,
               font=('Chalkboard', 14, 'bold'), fg="#47270f")
    output = StringVar()
    output.set(disp)
    out = Label(frame2, textvariable=output, bg="#85491b", bd=3,
                font=('Chalkboard', 14, 'bold'), fg="#47270f")
    sp5 = Label(frame2, text="\n", bg="#85491b", bd=3)
    in2 = Entry(frame2, bg="#85491b", bd=0, font=('Chalkboard', 12), fg="#2b1809", highlightcolor="#85491b",
                show="*", width=18)
    buttWord = Button(master=frame2, activeforeground="#1a0e05", activebackground="#542e11", bg="#754017",
                      fg="#2b1809", relief=GROOVE, justify="center", height=1, text="GUESS",
                      command=lambda: answerInput(in2))
    h5.grid()
    out.grid()
    in2.grid()
    sp5.grid()
    in2.grid()
    buttWord.grid()
    output.set(disp)
    out.grid()

    count = 6
    global guess, oldGuess
    while count > 0 and display != answer:
        flag = False
        if guess != oldGuess:
            for i in range(len(answer)):
                if answer[i] == guess:
                    display[i] = guess
                    disp = " ".join(display)  # Contains the word in list form with blanks
                    flag = True
            output.set(disp)
            root.update_idletasks()
            oldGuess = guess

            print(disp)
            print()
        else:
            continue
        if not flag:
            count = count - 1
            L[count]()

        print("Chances left:", count)

        if count == 0:
            print("Sorry you lost. The word was", answerIn)
    if count != 0:
        print("Well done you guessed the word")
    time.sleep(10)
    if mode == 1:
        clearScreen()
        # Would you like to play again or quit pop up
    elif mode == 2:
        clearScreen()
        twoPlayer(1)


def stand():
    draw.pendown()
    draw.forward(100)
    draw.backward(50)
    draw.left(90)
    draw.forward(250)
    draw.right(90)
    draw.forward(90)
    draw.right(90)
    draw.forward(30)
    draw.hideturtle()


def head():
    draw.showturtle()
    draw.right(90)
    draw.forward(20)
    draw.left(90)
    draw.forward(40)
    draw.left(90)
    draw.forward(40)
    draw.left(90)
    draw.forward(40)
    draw.left(90)
    draw.forward(20)
    draw.forward(20)
    draw.left(90)
    draw.forward(40)
    draw.left(90)
    draw.forward(20)
    draw.right(90)
    draw.hideturtle()


def hands():
    draw.showturtle()
    draw.forward(30)
    draw.right(87)
    draw.forward(42)
    draw.right(180)
    draw.forward(42)
    draw.right(6)
    draw.forward(42)
    draw.right(180)
    draw.forward(42)
    draw.left(93)
    draw.hideturtle()


def body():
    draw.showturtle()
    draw.forward(30)
    draw.right(37)
    draw.hideturtle()


def leg():
    draw.showturtle()
    draw.forward(42)
    draw.right(180)
    draw.forward(42)
    draw.right(106)
    draw.forward(42)
    draw.hideturtle()


def face():
    draw.showturtle()
    draw.penup()
    draw.left(180)
    draw.forward(42)
    draw.right(37)
    draw.forward(87)
    draw.left(90)
    draw.forward(8)
    draw.right(90)
    draw.pendown()
    draw.left(30)
    draw.forward(5)
    draw.backward(10)
    draw.forward(5)
    draw.right(90)
    draw.forward(5)
    draw.backward(10)
    draw.forward(5)
    draw.penup()
    draw.right(30)
    draw.forward(17)
    draw.left(30)
    draw.pendown()
    draw.forward(5)
    draw.backward(10)
    draw.forward(5)
    draw.left(90)
    draw.forward(5)
    draw.backward(10)
    draw.forward(5)
    draw.penup()
    draw.right(30)
    draw.backward(17)
    draw.right(90)
    draw.pendown()
    draw.forward(3)
    draw.backward(21)
    draw.forward(18)
    draw.right(85)
    draw.forward(4)
    draw.right(80)
    draw.forward(3)
    draw.right(80)
    draw.forward(3)
    draw.forward(1)
    draw.hideturtle()


def singlePlayer():
    answerList = ["world", "animation", "africa", "computer", "rickshaw", "physics", "chemistry", "inception", "header",
                  "grandfather", "avatar", "shampoo", "electrolysis", "orangutan", "flow", "rumble", "shambles",
                  "display", "international", "binder", "paperclip", "socket", "inferno", "archetype", "external",
                  "forgettable", "inject", "forlorn", "swap", "kernel", "wardrobe", "humour", "bomb", "terraform"]
    random.shuffle(answerList)
    answer1 = answerList[0]
    mainGame(answer1, 1)


def twoPlayer(n):
    clearFrame(frame2)
    if n == 1:
        turn = 2
    elif n == 2:
        turn = 1
    h1 = Label(frame2, text="————————————————\n PLAYER {} \n————————————————".format(n), bg="#85491b",
               bd=3, font=('Chalkboard', 14, 'bold'), fg="#47270f")
    h2 = Label(frame2, text="\nEnter your word", bg="#85491b", bd=3, font=('Chalkboard', 12, 'bold'), fg="#47270f")
    in1 = Entry(frame2, bg="#85491b", bd=0, font=('Chalkboard', 12), fg="#2b1809", highlightcolor="#85491b",
                show="*", width=18)
    sp4 = Label(frame2, text="\n", bg="#85491b", bd=3)
    buttIn = Button(master=frame2, activeforeground="#1a0e05", activebackground="#542e11", bg="#754017",
                    fg="#2b1809", relief=GROOVE, justify="center", height=1, text="SUBMIT",
                    command=lambda: twoPlayerInput(turn, in1))
    h1.pack()
    h2.pack()
    in1.pack()
    sp4.pack()
    buttIn.pack()


def twoPlayerInput(turn, inp):
    answerIn1 = inp.get()
    if turn == 1:
        print("Turn", 1)
        mainGame(answerIn1, 2)
        twoPlayer(1)
    elif turn == 2:
        print("Turn", 2)
        mainGame(answerIn1, 1)
        # end game


# Startup screen
spacer1 = Frame(root, bg="#754017")
frame1 = Frame(root, bg="#754017")
frame2 = Frame(root, bg="#85491b")
sp1 = Label(spacer1, text="                  ", bg="#754017", bd=3, font=('Chalkboard SE', 18, 'bold'))
l1 = Label(root, text="H A N G M A N", bg="#754017", bd=3, font=('Chalkboard SE', 18, "bold"), anchor=E, fg="#2b1809")
canvas = Canvas(master=root, width=300, height=300, bd=0)
turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("#346B31")
l2 = Label(frame2, text="————————————————\n SELECT MODE \n————————————————", bg="#85491b", bd=3,
           font=('Chalkboard', 14, "bold"), fg="#47270f")
sp2 = Label(frame2, text="", bg="#85491b", bd=3)
bSing = Button(master=frame2, relief=GROOVE, activeforeground="#1a0e05", activebackground="#542e11",
               bg="#754017", fg="#2b1809", justify="center", height=4, text="SINGLE\nPLAYER", width=8,
               command=singlePlayer)
sp3 = Label(frame2, text="\n", bg="#85491b", bd=3)
bDouble = Button(master=frame2, relief=GROOVE, activeforeground="#1a0e05", activebackground="#542e11",
                 bg="#754017", fg="#2b1809", justify="center", height=4, text="TWO\nPLAYER", width=8,
                 command=lambda: twoPlayer(2))
# Activating grids
spacer1.grid(row=0, column=8, sticky='NSEW')
frame1.grid(row=0, column=0, sticky='NSEW', columnspan=3)
frame2.grid(row=1, column=8, sticky='NSEW', rowspan=7)
sp1.grid()
l1.grid(row=0, column=3)
canvas.grid(row=1, column=0, rowspan=7, columnspan=4, sticky='NSEW')
l2.grid()
sp2.grid()
bSing.grid()
sp3.grid()
bDouble.grid()
# Starting Turtle
draw = turtle.RawTurtle(turtle_screen)
draw.penup()
draw.setpos(-125, -125)
draw.color("#FBF7F5")
draw.speed(1)
root.update_idletasks()
root.mainloop()
