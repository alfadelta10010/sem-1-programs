from sys import getrefcount

a = 10
print("The number 10 has been referenced to " + str(getrefcount(10)) + " times, before num")
num = 10
print("The number 10 has been referenced to " + str(getrefcount(10)) + " times")
print("The variable ID of a is " + str(id(a)) + " and the variable ID of num is " + str(id(num)))

# This principle does not always apply to floats, due to precision
b = 10.12
c = 10.12
print("The variable ID of b is " + str(id(b)) + " and the variable ID of c is " + str(id(c)))

# since list is mutable, the id of the list even after being changed stays the same
