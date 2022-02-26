def outer():
    a = 0
    b = 1

    def inner(n):
        nonlocal a, b
        i = 1
        while i <= n:
            print(a)
            c = a + b
            a = b
            b = c
            i = i + 1
        return inner


x = outer()
x(5)
