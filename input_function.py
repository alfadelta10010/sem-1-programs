# input function
# import sys
import sys

x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))
s = x + y
print("Result:", s)

# without int conversion, the strings get concatenated
#
# Enter number 1: 1
# Enter number 2: 2
# Result: 12

# eval function, to evaluate the entered expression
print(eval(input("Enter an expression: ")))

# to get a specific character in the string, we use indexes
print("The first character is", input("Enter an string: ")[0])

# taking input from command line
# q = int(sys.argv[1])  # index 0 is the file name
# w = int(sys.argv[2])
# print(q+w)

# split function
x, y = input("Enter two nos.: ").split(sep=";")  # default separator is <space>
print(x)
print(y)

str = input("Enter a string")
x = len(str)
print(x)

x = sys.stdin.readline()
print(x)
print(len(x))
