# 5. Write a python program to find the longest words in a file.
filename = input("Enter file name: ")
with open(filename, 'r') as infile:
    words = infile.read().split()
max_len = len(max(words, key=len))
print([word for word in words if len(word) == max_len])
