# 4) Write a python program to find the gravitational forces acting
# between two objects of given masses
m1 = float(input("Enter the mass of the 1st body: "))
m2 = float(input("Enter the mass of the 2nd body: "))
G = 6.674 * 10 ** -11
r = float(input("Enter the distance between the two bodies: "))
f = (G * m1 * m2) / r ** 2
print("The Gravitational force between the two bodies is {} N".format(f))
