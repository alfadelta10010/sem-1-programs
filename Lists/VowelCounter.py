# wap to count number of vowels in a given string and store it in a separate list
s = input("Enter a string: ")
l1 = []
v = ["a", "e", "i", "o", "u"]
cntv = 0
for i in s:
    if i in v:
        cntv = cntv+1
        l1.append(i)
print(l1)
print(cntv)

