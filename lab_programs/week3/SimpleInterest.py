# 1) Suppose a person wants to calculate the simple interest in the
# account he has taken for specified number of years. Read values
# from the user
p = float(input("Enter the value of the principal: "))
r = float(input("Enter the rate of interest: "))
t = int(input("Enter the number of years: "))

si = (p * r * t)/100
print("Your simple interest comes up to ₹{0:2.2f}".format(si))
