# WAP to arrange the string character such that the lower case letter should come first
s1 = "pYthONk"
lower = []
upper = []
for i in s1:
    if i.islower():
        lower.append(i)
    else:
        upper.append(i)
print("".join(lower+upper))
