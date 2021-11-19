# 3. WAP that will read three numbers into variables named a, b and c
# and print a message informing the user whether they are a pythagorean
# triplet.
a, b, c = input("Enter three numbers: ").split(sep=" ")
a = int(a)
b = int(b)
c = int(c)
if a > b and a > c:
    largest = a
    rhs = c ** 2 + b ** 2
elif b > c:
    largest = b
    rhs = c ** 2 + a ** 2
else:
    largest = c
    rhs = a ** 2 + b ** 2
if rhs == (largest ** 2):
    print("The numbers are a pythagorean triplet")
else:
    print("The numbers are not a pythagorean triplet")
