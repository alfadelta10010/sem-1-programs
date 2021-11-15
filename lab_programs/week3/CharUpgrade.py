# 5) Write a python program to read 4 characters separately from the
# user. Convert every character to its next alphabet
c1, c2, c3, c4 = input("Enter 4 characters, separated by spaces: "
                       ).split(sep=" ")
c1 = chr(ord(c1)+1)
c2 = chr(ord(c2)+1)
c3 = chr(ord(c3)+1)
c4 = chr(ord(c4)+1)
print("The changed characters are: {0}, {1}, {2}, {3}.".format(c1, c2,
                                                               c3, c4))
