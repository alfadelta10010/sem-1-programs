# 3) Write a python program which accepts the radius of a sphere and
# computes the volume and surface area.
import math

r = float(input("Please enter the radius of the sphere: "))
sa = 4 * math.pi * r ** 2
v = (4 * math.pi * r ** 3) / 3
print("The sphere with radius {0} has a surface area of {1:3.3f} sq.units and volume of {2:3.3f} cubic units.".format
      (r, sa, v))
