# 7. WAP to add the digits of a positive number repeatedly until the result has a single digit. if 59, 5+9=14, 1+4=5
s = int(input("Enter the number: "))
while s > 9:
    s = (s - 1) % 9 + 1
print("result:", s)
