# 3. WAP that will read three numbers into variables named a, b and c
# and print a message informing the user whether they are a pythagorean
# triplet.
a, b, c = input("Enter three numbers: ").split(sep=" ")
if int(a) > int(b) and int(a) > int(c):
    largest = int(a)
    rhs = int(c) ** 2 + int(b) ** 2
elif b > c:
    largest = int(b)
    rhs = int(c) ** 2 + int(a) ** 2
else:
    largest = int(c)
    rhs = int(a) ** 2 + int(b) ** 2
if rhs == (largest ** 2):
    print("The numbers are a pythagorean triplet")
else:
    print("The numbers are not a pythagorean triplet")
