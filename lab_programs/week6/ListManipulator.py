# 2. Write a program to perform the following
# operations using given list as input:
# a) Create separate lists of strings and numbers
# b) Sort the strings list in ascending order
# c) Sort the number list from lowest to highest
# d) Sort the number list from highest to lowest

listA = ["Mobile", 21312, "Laptop", 310.12, "TV"]
str_items = []; num_items = []; ascend = []
for item in listA:
    if isinstance(item, str):
        str_items.append(item)
    elif isinstance(item, int) or isinstance(item, float):
        num_items.append(item)
for i in str_items:
    ascend.append(i.lower())
ascend.sort(); num_items.sort()
print("Ascending order:", ascend)
print("Lowest to highest:", num_items)
num_items.sort(reverse=True)
print("Highest to lowest:", num_items)
