# 4) Use callback to find sum, double and triple the given number
def sum1(x):
    s = 0
    for i in range(1, x + 1):
        s = s + i
    print("Sum is", s)


def doubleIt(x):
    print("Double of", x, "is", x * 2)


def tripleIt(x):
    print("Triple of", x, "is", x * 3)


def someAction(i, cb):
    cb(i)


num = int(input("Enter a number: "))
someAction(num, sum1)
someAction(num, doubleIt)
someAction(num, tripleIt)
