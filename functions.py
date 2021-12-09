"""
def hello(s):
    print("Hello", s)


hello(input("Please enter your name: "))
hello(input())


'''                        '''


def display():
    print("During function call")


print("Before function call")
display()
print("After function call")

print(display)
display1 = display
display1()
del display
# display()
display1()
"""


def f1(n):
    print(n)
    if n != 0:
        return f1(n - 1)


def fibby(n1):
    a, b = 0, 1
    while a < n1:
        print(a, end=" ")
        a, b = b, a + b


# fibby(1000)
