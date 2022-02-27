# 2) b) Given a list of numbers, find maximum in the list
import functools
l = [23, 45, 12, 47, 54]
print(functools.reduce(lambda x, y: x if x > y else y, l))
