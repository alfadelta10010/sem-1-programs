# 1) Write a program to count the number of Vowels in a given string and store in separate list.
st1 = input("Enter a string: ")
new_vow = []
for i in st1:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        new_vow.append(i)
print("Vowels:", new_vow)
