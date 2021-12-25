# 3. Write a program to print a dictionary where the keys are numbers between
# 1 and 15 and the values are cube of keys.

cube = dict()
for x in range(1, 16):
    cube[x] = pow(x, 3)
print("The dictionary with cubed numbers from 1 to 15 is:", cube)
