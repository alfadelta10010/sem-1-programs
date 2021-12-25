"""
def hello(s):
    print("Hello", s)


hello(input("Please enter your name: "))
hello(input())




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


# old
"""

# fibby(1000)
# if outer function is deleted, inner function is still accessible with its address
"""


# WAP to find sum of two numbers using closure
def a1(a, b):
    def a2():
        print(a + b)

    return a2
a = a1(10, 20)
a()

def f4(c):
    def f5():
        while c > 0:
            c = c - 1
            print(c)
    return f5
x = f4(10)
x()
