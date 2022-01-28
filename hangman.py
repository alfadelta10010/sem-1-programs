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
canvas = Canvas(master=root, width=400, height=400)
turtle_screen = turtle.TurtleScreen(canvas)
turtle_screen.bgcolor("red")
canvas.grid(padx=5, pady=5, row=0, column=0, rowspan=10, columnspan=10)  # , sticky='nsew')
draw = turtle.RawTurtle(turtle_screen)
draw.penup()
draw.setpos(-175, -175)
draw.color("black")
draw.speed(1)


def clearScreen():
    if os.name in ('nt', 'dos'):
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)


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


def mainGame(answerIn):
    answer = list(answerIn)
    display = []
    display.extend(answer)
    for i in range(len(display)):
        w = 0
        for j in range(len(vowelsList)):
            if display[i] == vowelsList[j]:
                w = 1
        if w == 0:
            display[i] = "_"
    print(" ".join(display))
    print()

    count = 6

    while count > 0 and display != answer:
        guess = input("Please guess a letter: ")
        flag = False
        for i in range(len(answer)):
            if answer[i] == guess:
                display[i] = guess
                flag = True
        print(" ".join(display))
        print()

        if not flag:
            count = count - 1
            L[count]()
        print("Chances left:", count)

        if count == 0:
            print("Sorry you lost. The word was", answer)
    if count != 0:
        print("Well done you guessed the word")
    time.sleep(10)


vowelsList = ["a", "e", "i", "o", "u"]
L = [face, leg, body, hands, head, stand]
answerList = ["world", "animation", "africa", "computer", "rickshaw", "physics", "chemistry", "inception", "header",
              "grandfather", "avatar", "shampoo", "electrolysis", "orangutan", "flow", "rumble", "shambles",
              "display", "international", "binder", "paperclip", "socket", "inferno", "archetype", "external",
              "forgettable", "inject", "forlorn", "swap", "kernel", "wardrobe", "humour", "bomb", "terraform"]
print("Lets play Hangman! \n1) Play Single player \n2) Play with a friend")
mode = int(input("Please select your mode (1 or 2): "))
if mode == 1:
    random.shuffle(answerList)
    answer1 = answerList[0]
    mainGame(answer1)
    clearScreen()
elif mode == 2:
    answerIn1 = input("Player 2: Enter the word: ")
    clearScreen()
    mainGame(answerIn1)
    clearScreen()
    turtle.clear()
    draw.setpos(-175, -175)
    draw.speed(1)
    answerIn2 = input("Player 1: Enter the word: ")
    answer2 = list(answerIn2)
    clearScreen()
    mainGame(answer2)
else:
    print("You did not enter a correct choice. Terminating program...")
    time.sleep(10)
