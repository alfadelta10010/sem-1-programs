# WAP to define a function to display any two numbers with a function
def function(n):
    print("Val in function", n)


def interface(fn, m):
    fn(m)


interface(function, 10)
interface(function, 20)
