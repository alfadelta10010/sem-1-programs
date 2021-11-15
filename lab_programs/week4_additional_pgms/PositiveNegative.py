# WAP to display if the number entered is Positive or Negative
n = int(input("Enter a number: "))
if n > 0:
    print("{0} is a positive number".format(n))
elif n < 0:
    print("{0} is a negative number".format(n))
else:
    print("You entered 0. Did you think you could be sneaky?")
