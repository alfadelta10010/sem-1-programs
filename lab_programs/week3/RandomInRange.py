# 9) Generate a random floating point number within a range
import random
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
ranNo = random.uniform(n1, n2)
print("Random number between {} and {} is {}".format(n1, n2, ranNo))
