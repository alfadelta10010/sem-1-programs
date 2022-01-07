# 4. The program takes a file name from the user
# and reads the contents of the file in reverse order.
filename = input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())
