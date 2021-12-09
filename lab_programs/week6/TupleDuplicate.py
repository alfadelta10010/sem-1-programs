# 7) Write a Python program to find the repeated items of a tuple.
tuple1 = (2, 4, 5, 6, 2, 3, 4, 4, 7)
n = int(input("Enter number to check: "))
count_rep = tuple1.count(n)
print("It is present", count_rep, "times in tuple")
3