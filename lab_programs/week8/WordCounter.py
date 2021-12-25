# 1.The program takes the file name from the user
# and counts number of words in that file.
fn = input("Enter file name: ")
num_words = 0

with open(fn, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)
