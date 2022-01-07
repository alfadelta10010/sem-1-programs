# 7.Write a program in Python that transforms the
# content of the file by writing each word in a separate line

f = open("randomtextfile.txt", 'r')  # opening file in read mode
content = f.read()  # getting the file content
# converting the content to a list
L = content.split()
f.close()
# opening file in write mode
f = open("myfile.txt", 'w')
# building the content file
for word in L:
    f.write(word + "\n")
f.close()
