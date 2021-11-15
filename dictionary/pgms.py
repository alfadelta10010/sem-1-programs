# WAP to add a key to a dictionary
"""
# WAP to concatenate a dictionary
d1 = {1: 10, 2: 20}
d2 = {3: 30, 4: 40}
d3 = {5: 50, 6: 60}
d4 = {}
for i in (d1, d2, d3):
    d4.update(i)
print(d4)
"""
# WAP to iterate a dictionary and print key value pair as "key -> value"
d1 = {1: 10, 2: 20}
for key, value in d1.items():
    print("{} -> {}".format(key, d1[key]))

# WAP to sum all the items in dictionary
# (sum function)
