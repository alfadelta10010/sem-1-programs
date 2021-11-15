import math
print("=== Calculate Area of Shape ===")
while True:
    name = input("Enter the name of the shape whose area you want to find: ")
    name = name.lower()  # to make the name lowercase for checking
    if name == "square":
        s = float(input("Enter side length of the square: "))
        square_area = s ** 2
        print("Area of the square of side {} is {} sq.units".format(s, square_area))
    elif name == "rectangle":
        length = float(input("Enter rectangle's length: "))
        breadth = float(input("Enter rectangle's breadth: "))
        rect_area = length * breadth
        print("Area of the rectangle with dimensions {} x {} is {} sq.units".format(length, breadth, rect_area))
    elif name == "circle":
        r = float(input("Enter radius of the circle: "))
        cir_area = math.pi * (r ** 2)
        print("Area of the circle with radius {0} is {1:3.3f} sq.units".format(r, cir_area))
    elif name == "triangle":
        tri_ch = input("Using base length and height? (y/n): ")
        if tri_ch == "y" or "Y":
            b = float(input("Enter the base length of the triangle: "))
            h = float(input("Enter the height of the triangle: "))
            tri_area = 0.5 * b * h
        else:
            s1 = float(input("Enter the length of side 1: "))
            s2 = float(input("Enter the length of side 2: "))
            s3 = float(input("Enter the length of side 3: "))
            sem = (s1 + s2 + s3) / 3
            tri_area = math.sqrt(sem * (sem - s1) * (sem - s2) * (sem - s3))
        print("Area of the triangle is {} sq.units".format(tri_area))
    elif name == "parallelogram":
        b = float(input("Enter the value of base of the parallelogram: "))
        h = float(input("Enter the value of height of the parallelogram: "))
        par_area = b * h
        print("Area of the parallelogram is {} sq.units".format(par_area))
    else:
        print("404: Shape not found")
    c = input("Would you like to try again? (y/n): ")
    if c == "n" or c == "N":
        break
