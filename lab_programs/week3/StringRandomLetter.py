# 8) Write a python program
# a) to get a single random character from a specified string
import random
name = input("Enter a word: ")
ch = random.choice(name)
print("Random letter from", name, "is", ch)
