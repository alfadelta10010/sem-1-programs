# 3. Write a Python program to read a random line from a file.
from random import choice
filename = input("Enter the file name: ")
fd = open(filename, 'r')
content = fd.read()
lines = content.splitlines()

print("Line:", choice(lines))
fd.close()
