import random
import turtle
from tkinter import *

root = Tk()
guess = ""
oldGuess = ""
done = False
turn = 0
vowelsList = ["a", "e", "i", "o", "u"]
display = []
answer = []
dispString = ""
answerIn = ""
output = StringVar()
COut = IntVar()
buttWord = Button()
count = 6

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=9)
root.columnconfigure(1, weight=8)
root.title('Hangman')


def redirect():  # no. 14
    global guess, oldGuess, done, dispString, display, answer, answerIn, output, COut, count
    guess = ""
    oldGuess = ""
    done = False
    display = []
    answer = []
    dispString = ""
    answerIn = ""
    output = StringVar()
    COut = IntVar()
    count = 6
    clearFrame(frame2)
    h2 = Label(frame2, text="————————————————\n SELECT MODE \n————————————————", bg="#85491b", bd=3,
               font=('Chalkboard', 14, "bold"), fg="#47270f")
    spacer2 = Label(frame2, text="", bg="#85491b", bd=3)
    bSingl = Button(master=frame2, relief=GROOVE, activeforeground="#1a0e05", activebackground="#542e11",
                    bg="#754017", fg="#2b1809", justify="center", height=3, text="SINGLE\nPLAYER", width=8,
                    command=singlePlayer)
    spacer3 = Label(frame2, text="", bg="#85491b", bd=3)
    bDoubl = Button(master=frame2, relief=GROOVE, activeforeground="#1a0e05", activebackground="#542e11",
                    bg="#754017", fg="#2b1809", justify="center", height=3, text="TWO\nPLAYER", width=8,
                    command=lambda: twoPlayer(2))
    h2.grid()
    spacer2.grid()
    bSingl.grid()
    spacer3.grid()
    bDoubl.grid()
    clearTurtle()


def stand():  # no. 8
    global draw
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


def head():  # no. 9
    global draw
    draw.pendown()
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


def hands():  # no. 10
    global draw
    draw.pendown()
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


def body():  # no. 11
    global draw
    draw.pendown()
    draw.showturtle()
    draw.forward(30)
    draw.right(37)
    draw.hideturtle()


def leg():  # no. 12
    global draw
    draw.pendown()
    draw.showturtle()
    draw.forward(42)
    draw.right(180)
    draw.forward(42)
    draw.right(106)
    draw.forward(42)
    draw.hideturtle()


def face():  # no. 13
    global draw
    draw.pendown()
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


def clearTurtle():  # no. 7
    global turtle_screen, draw
    turtle_screen.resetscreen()
    draw.penup()
    turtle_screen.bgcolor("#346B31")
    draw.setpos(-125, -125)
    draw.color("#FBF7F5")
    draw.speed(2)
    draw.pendown()


def clearFrame(frame):  # no. 6
    for widget in frame.winfo_children():
        widget.destroy()


def singlePlayer():  # no. 5
    answerList = ["world", "animation", "africa", "computer", "rickshaw", "physics", "chemistry", "inception", "header",
                  "grandfather", "avatar", "shampoo", "electrolysis", "orangutan", "flow", "rumble", "shambles",
                  "display", "international", "binder", "paperclip", "socket", "inferno", "archetype", "external",
                  "forgettable", "inject", "forlorn", "swap", "kernel", "wardrobe", "humour", "bomb", "terraform"]
    random.shuffle(answerList)
    answer1 = answerList[0]
    mainGame(answer1, 1)


def answerInput(inp, modeIN):  # no. 4
    global guess, oldGuess
    oldGuess = guess
    guess = inp.get()
    inp.delete(0, END)
    mainGameP2(modeIN)


def mainGame(answerI, mode):  # no. 1
    global guess, vowelsList, display, answer, answerIn, dispString, L, output, buttWord
    answerIn = answerI
    clearFrame(frame2)
    answer = list(answerIn)
    display.extend(answer)  # Will contain the word in list form
    for i in range(len(display)):
        w = 0
        for j in range(len(vowelsList)):
            if display[i] == vowelsList[j]:
                w = 1
        if w == 0:
            display[i] = "_"
    dispString = " ".join(display)  # Contains the word in list form with blanks
    output.set(dispString)
    COut.set(count)
    h5 = Label(frame2, text="————————————————\n GUESS THE WORD \n————————————————", bg="#85491b", bd=3,
               font=('Chalkboard', 14, 'bold'), fg="#47270f")
    out = Label(frame2, textvariable=output, bg="#85491b", bd=3,
                font=('Chalkboard', 14, 'bold'), fg="#47270f")
    h6 = Label(frame2, text="\n Chances left: ", bg="#85491b", bd=3,
               font=('Chalkboard', 14, 'bold'), fg="#47270f")
    outC = Label(frame2, textvariable=COut, bg="#85491b", bd=3,
                 font=('Chalkboard', 16, 'bold'), fg="#47270f")
    in2 = Entry(frame2, bg="#754017", bd=2, font=('Chalkboard', 12), fg="#2b1809", highlightcolor="#85491b",
                width=4, justify=CENTER)
    sp5 = Label(frame2, text="\n", bg="#85491b", bd=3)
    buttWord = Button(master=frame2, activeforeground="#1a0e05", activebackground="#542e11", bg="#754017",
                      fg="#2b1809", relief=GROOVE, justify="center", height=1, text="GUESS",
                      command=lambda: answerInput(in2, mode))
    h5.grid()
    out.grid()
    h6.grid()
    outC.grid()
    in2.grid()
    sp5.grid()
    buttWord.grid(padx=20, pady=10)


def mainGameP2(gameMode):  # no. 3
    global guess, oldGuess, done, dispString, display, answer, answerIn, output, COut, count
    won = False
    while count > 0 and display != answer and guess != oldGuess:
        done = False
        flag = False
        for i in range(len(answer)):
            if answer[i] == guess:
                display[i] = guess
                flag = True
        oldGuess = guess
        dispString = " ".join(display)
        output.set(dispString)
        root.update_idletasks()
        if not flag:
            count = count - 1
            COut.set(count)
            root.update_idletasks()
            L[count]()
        if count == 0:
            won = False
            done = True
    if display == answer and count != 0:
        won = True
        done = True
    if done:
        if gameMode == 1:
            clearFrame(frame2)
            if won:
                h9 = Label(frame2, text="————————————————\n YOU WON! \n————————————————", bg="#85491b", bd=3,
                           font=('Chalkboard', 14, 'bold'), fg="#47270f", anchor=CENTER)
            else:
                h9 = Label(frame2, text="————————————————\n YOU LOST :( \n————————————————", bg="#85491b", bd=3,
                           font=('Chalkboard', 14, 'bold'), fg="#47270f", anchor=CENTER)
            h10 = Label(frame2, text="The word was:", bg="#85491b", bd=3,
                        font=('Chalkboard', 14, 'bold'), fg="#47270f", anchor=CENTER)
            output.set(("".join(answer)))
            root.update_idletasks()
            out = Label(frame2, textvariable=output, bg="#85491b", bd=3,
                        font=('Chalkboard', 14, 'bold'), fg="#47270f")
            bAgain = Button(master=frame2, relief=GROOVE, activeforeground="#1a0e05", activebackground="#542e11",
                            bg="#754017", fg="#2b1809", justify="center", height=3, text="PLAY\nAGAIN", width=8,
                            command=redirect)
            sp5 = Label(frame2, text="", bg="#85491b", bd=3)
            bQuit = Button(master=frame2, relief=GROOVE, activeforeground="#1a0e05", activebackground="#542e11",
                           bg="#754017", fg="#2b1809", justify="center", height=3, text="QUIT", width=8,
                           command=root.destroy)
            h9.grid()
            h10.grid()
            out.grid()
            bAgain.grid(padx=20, pady=10)
            sp5.grid()
            bQuit.grid(padx=20, pady=10)
        elif gameMode == 2:
            clearTurtle()
            clearFrame(frame2)
            if won:
                h9 = Label(frame2, text="————————————————\n YOU WON! \n————————————————", bg="#85491b", bd=3,
                           font=('Chalkboard', 14, 'bold'), fg="#47270f", anchor=CENTER)
            else:
                h9 = Label(frame2, text="————————————————\n YOU LOST :( \n————————————————", bg="#85491b", bd=3,
                           font=('Chalkboard', 14, 'bold'), fg="#47270f", anchor=CENTER)
            h10 = Label(frame2, text="The word was:", bg="#85491b", bd=3,
                        font=('Chalkboard', 14, 'bold'), fg="#47270f", anchor=CENTER)
            output.set(("".join(answer)))
            root.update_idletasks()
            out = Label(frame2, textvariable=output, bg="#85491b", bd=3,
                        font=('Chalkboard', 14, 'bold'), fg="#47270f")
            h9.grid()
            h10.grid()
            out.grid()
            guess = ""
            oldGuess = ""
            done = False
            display = []
            answer = []
            dispString = ""
            answerIn = ""
            output = StringVar()
            COut = IntVar()
            count = 6
            clearTurtle()
            sp6 = Label(frame2, text="\n\n", bg="#85491b", bd=3)
            cont = Button(master=frame2, activeforeground="#1a0e05", activebackground="#542e11", bg="#754017",
                          fg="#2b1809", relief=GROOVE, justify="center", height=1, text="CONTINUE",
                          command=lambda: twoPlayer(1))
            sp6.grid()
            cont.grid(padx=20, pady=10)


def twoPlayer(n):  # no. 2
    clearFrame(frame2)
    global turn
    if n == 1:
        turn = 2
    elif n == 2:
        turn = 1
    h1 = Label(frame2, text="————————————————\n PLAYER {} \n————————————————".format(n), bg="#85491b",
               bd=3, font=('Chalkboard', 14, 'bold'), fg="#47270f")
    h2 = Label(frame2, text="\nEnter your word", bg="#85491b", bd=3, font=('Chalkboard', 12, 'bold'), fg="#47270f")
    in1 = Entry(frame2, bg="#754017", bd=2, font=('Chalkboard', 12), fg="#2b1809", highlightcolor="#85491b",
                show="*", width=18, justify=CENTER)
    sp4 = Label(frame2, text="\n", bg="#85491b", bd=3)
    buttIn = Button(master=frame2, activeforeground="#1a0e05", activebackground="#542e11", bg="#754017",
                    fg="#2b1809", relief=GROOVE, justify="center", height=1, text="SUBMIT",
                    command=lambda: twoPlayerInput(in1))
    h1.pack()
    h2.pack()
    in1.pack()
    sp4.pack()
    buttIn.pack(padx=20, pady=10)


def twoPlayerInput(inp):
    global turn
    answerIn1 = inp.get()
    if turn == 1:
        mainGame(answerIn1, 2)
    if turn == 2:
        mainGame(answerIn1, 1)


# Startup screen
spacer1 = Frame(root, bg="#754017")
frame1 = Frame(root, bg="#754017")
frame2 = Frame(root, bg="#85491b")
sp1 = Label(spacer1, text="                  ", bg="#754017", bd=3, font=('Chalkboard SE', 18, 'bold'))
l1 = Label(root, text="H A N G M A N", bg="#754017", bd=3, font=('PHOSPHATE', 22), anchor=E, fg="#2b1809")
canvas = Canvas(master=root, width=300, height=300, bd=0)
turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("#346B31")
l2 = Label(frame2, text="————————————————\n SELECT MODE \n————————————————", bg="#85491b", bd=3,
           font=('Chalkboard', 14, "bold"), fg="#47270f")
sp2 = Label(frame2, text="", bg="#85491b", bd=3)
bSing = Button(master=frame2, relief=GROOVE, activeforeground="#1a0e05", activebackground="#542e11",
               bg="#754017", fg="#2b1809", justify="center", height=3, text="SINGLE\nPLAYER", width=8,
               command=singlePlayer)
sp3 = Label(frame2, text="", bg="#85491b", bd=3)
bDouble = Button(master=frame2, relief=GROOVE, activeforeground="#1a0e05", activebackground="#542e11",
                 bg="#754017", fg="#2b1809", justify="center", height=3, text="TWO\nPLAYER", width=8,
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
L = [face, leg, body, hands, head, stand]
draw.setpos(-125, -125)
draw.color("#FBF7F5")
draw.speed(2)

root.mainloop()
