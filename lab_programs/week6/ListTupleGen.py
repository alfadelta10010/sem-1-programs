# 6) Write a python program which accepts a sequence of comma-separated
# numbers from console and generate a list and a tuple which contains
# every number.
values = input("Enter values separated by commas: ")
ll = values.split(",")
t = tuple(ll)
print("Tuple:", t)
print("List:", ll)
