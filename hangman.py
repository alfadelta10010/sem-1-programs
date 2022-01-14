# One player thinks of a word, phrase or sentence and the other tries to guess it
# by suggesting letters within a certain number of guesses.  If the guessing player
# suggests a letter which occurs in the word, the other player writes it in all its
# correct positions. If the suggested letter does not occur in the word, the other
# player draws one element of a hanged stick figure as a tally mark.

import random
import time
import turtle
import os
turtle.color("black")
turtle.speed(1)


def clearScreen():
    if os.name in ('nt', 'dos'):
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)


def stand():
    turtle.forward(100)
    turtle.backward(50)
    turtle.left(90)
    turtle.forward(250)
    turtle.right(90)
    turtle.forward(90)
    turtle.right(90)
    turtle.forward(30)


def head():
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)


def hands():
    turtle.forward(30)
    turtle.right(87)
    turtle.forward(42)
    turtle.right(180)
    turtle.forward(42)
    turtle.right(6)
    turtle.forward(42)
    turtle.right(180)
    turtle.forward(42)
    turtle.left(93)


def body():
    turtle.forward(30)
    turtle.right(37)


def leg():
    turtle.forward(42)
    turtle.right(180)
    turtle.forward(42)
    turtle.right(106)
    turtle.forward(42)


def face():
    turtle.penup()
    turtle.left(180)
    turtle.forward(42)
    turtle.right(37)
    turtle.forward(87)
    turtle.left(90)
    turtle.forward(8)
    turtle.right(90)
    turtle.pendown()
    turtle.left(30)
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.right(90)
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.penup()
    turtle.right(30)
    turtle.forward(17)
    turtle.left(30)
    turtle.pendown()
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.backward(10)
    turtle.forward(5)
    turtle.penup()
    turtle.right(30)
    turtle.backward(17)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(3)
    turtle.backward(21)
    turtle.forward(18)
    turtle.right(85)
    turtle.forward(4)
    turtle.right(80)
    turtle.forward(3)
    turtle.right(80)
    turtle.forward(3)
    turtle.forward(1)
    turtle.hideturtle()


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
            print("Sorry you lost. The word was", answerIn)
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
    answerL = list(answerList[0])
    mainGame(answerL)
    clearScreen()
elif mode == 2:
    answerIn1 = input("Player 2: Enter the word: ")
    clearScreen()
    mainGame(answerIn1)
    clearScreen()
    turtle.clearscreen()
    turtle.speed(1)
    answerIn2 = input("Player 1: Enter the word: ")
    answer2 = list(answerIn2)
    clearScreen()
    mainGame(answer2)
else:
    print("You did not enter a correct choice. Terminating program...")
    time.sleep(10)

