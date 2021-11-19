# 5. WAP to read the values of a, b, c and produce a message saying how many roots the quadratic equation
# has and their forms
# if d == 0, return real and equal, d > 0, return real ad distinct, d < 0, return imaginary
# if imaginary, sqrt(-d)/2a = imaginary and -b/2a = real, else imaginary = sqrt(d)/2a
import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
d = math.sqrt(abs(b**2 - 4*a*c))
if d > 0:
    print("Two distinct roots")
elif d < 0:
    print("Two imaginary roots")
else:
    print("Distinct and equal roots")
