"""
List comprehension
[<expression> <iterative statement> <condition>]
"""

list1 = [i for i in range(1, 11)]
listOdd = [i for i in range(1, 11) if i % 2 != 0]  # aka for i in range(1, 11, 2)
listEven = [i for i in range(1, 11) if i % 2 == 0]  # aka for i in range(1, 11, 2)
l3 = [(i, j) for i in listOdd for j in listEven]
# print(l3)
l4 = [(listOdd[n], listEven[n]) for n in range(0, 5)]
l5 = [i for i in zip(listOdd, listEven)]
# print(l5)
fruits = ["mango", "apple", "kiwi", "watermelon", "grape", "orange"]
aFruits = [i for i in fruits if "a" in i]
# print(aFruits)
bigFruits = [i.upper() for i in fruits]
# print(bigFruits)
num1 = [28.0, -23.54, -10.0, 54.67]
noZero = [i if i > 0 else 0 for i in num1]
# print(noZero)

# create a list of tuples having a number and it's square
squareTuple = [(i, i * i) for i in range(1, 11)]
print(squareTuple)
# create a list of strings and its length
strings = ["wala", "walala", "wololololo"]
stringLength = [(i, len(i)) for i in strings]
print(stringLength)
# create a list of string whose length exceeds five

# create a list of squares of number from 0 to 4

# create a list of squares of numbers from 0 to 9 which are divisible by 2


l1 = [1, 2, 3, 4, 5]


def double(n):
    return n, n**n


l2 = [double(i) for i in l1]
print(l2)