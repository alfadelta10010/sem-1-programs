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
#display()
display1()

