# Iterators
num = [7, 8, 9, 5, 6]
# num is iterable object, iterable object doesn't have any iteration state
# iter() and next()
# xyz = iter(num)  # iterator object has iteration state
'''
print(xyz)  # <list_iterator object at 0x7feaac9a6fd0>
print(xyz.__next__())  # 7
print(xyz.__next__())  # 8
print(xyz.__next__())  # 9
print(xyz.__next__())  # 5
print(xyz.__next__())  # 6
'''


# print(next(xyz))  # 7


# Class: blueprint(common feature and functionality)
# objects: copy or instance of a class)

class Ten:
    def __iter__(self):
        self.n = 10
        return self

    def __next__(self):
        if self.n <= 20:
            value = self.n
            self.n = self.n + 2
            return value
        else:
            raise StopIteration


xyz = Ten()  # iterable object
abc = iter(xyz)  # iterator object
for i in abc:
    print(i)


# Generators - TO create your own iterator object
# It is a special type of function
# yield keyword instead of return keyword
def simple():
    yield 1
    yield 2
    yield 5


for i in simple():
    print(i)


def ten():
    # yield 5
    n = 1
    while n <= 10:
        yield n * n  # 1
        n += 1


a = ten()  # a is iterator object
print(a)
print(next(a))
for i in a:
    print(i)


# to generate fibo series
def fib1(n):
    a = 0
    b = 1
    while a <= n:
        yield a
        a, b = b, a + b


# If you don't want to you use
x = int(input("Enter the limit: "))
a = fib1(x)
for i in a:
    print(i)
