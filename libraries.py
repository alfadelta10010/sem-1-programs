import math

print(dir(math))
print(math.ceil(3.75))
print(math.ceil(3.23))
print(math.floor(3.23))
print(math.floor(3.999999))
print(math.sqrt(4))
print(math.sqrt(abs(-4)))  # math domain error
print(math.gcd(5, 25))
print(math.pi)
print(math.e)
print(math.exp(10))
print(math.factorial(3))
print(math.factorial(abs(-3)))  # value error
print()

import random
print(dir(random))
print(random.random())  # between 0 and 1
print(random.randint(5, 10))  # between given numbers, including them
print(random.randrange(0, 60, 5))  # random number out of (0, 5, 10, 15, 20...)
a = [34, 5, 6, 1]
print(random.choice(a))  # one random value from list a
print(random.choices(a, k=2))  # k random values from a
print(random.uniform(5, 10))  # number right in between the two numbers
print()

from adder_module import adder
e = int(input("Enter no. 1: "))
f = int(input("Enter no. 2: "))
print(adder(e, f))
