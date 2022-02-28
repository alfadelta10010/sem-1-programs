# 2) Define a user define type named Shape. Derive a type square from shape. The square takes length
# as an argument. Add a function area() in both types. Shape's area is 0 by default. Write the
# implementation for the following interface
class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, lIn):
        self.len = lIn

    def area(self):
        return self.len * self.len


s1 = Square(3)
print(s1.area())
