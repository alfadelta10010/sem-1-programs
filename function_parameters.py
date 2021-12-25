def change(x):  # formal parameter
    x = x + 1
    print("Nex X:", x)
    print("New X ID:", id(x))


def change2(x):  # formal parameter
    x[1] = x[1] + 1
    print("Nex X:", x)
    print("New X ID:", id(x))


a = 10
print("OG X:", a)
print("OG X ID: ", id(a))
change(a)  # actual argument

a = [10, 11, 12]
print("OG X:", a)
print("OG X ID:", id(a))
change2(a)  # actual argument


# Write a function
def fucn(*c):
    print(c)


fucn()
fucn(1)
fucn(1, 2)
fucn(1, 2, "abc")


def func(aa, b, *c, **cc):  # *c = tuple, **c = dictionary
    print(aa, b, c, cc)


func(2, 3, 4, 5, 6, red="r", white="w")
