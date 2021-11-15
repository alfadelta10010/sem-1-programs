# WAP to perform triangle classification based on length of sides entered

a = int(input("Enter length of Side A: "))
b = int(input("Enter length of Side B: "))
c = int(input("Enter length of Side C: "))

if a == b and a == c:
    print("Your triangle is an equilateral triangle")
elif a == b or a == c:
    print("Your triangle is an isosceles triangle")
else:
    print("Your triangle is a scalene triangle")
