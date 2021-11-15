# WAP to display grade of student

m = int(input("Enter your marks: "))
if m <= 100 and m > 80:
    print("You get grade A")
elif m <= 80 and m > 60:
    print("You get grade B")
elif m <= 60 and m > 40:
    print("You get grade C")
else:
    print("I am sorry for your loss of life")
