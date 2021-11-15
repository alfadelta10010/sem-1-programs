# WAP to remove duplicates from list
a = [89, 0, 10, 15, 23, 10]

x = list(set(a))
print(x)
print(type(x))

unique = []
for i in a:
    if i not in unique:
        unique.append(i)
print(unique)

