# 1) b) Add "ing" to all the elements of the
def update(n):
    return n + "ing"
def mymap(func, list1):
    result = []
    for i in list1:
        result.append(func(i))
    return result
l1 = ["walk", "eat", "sleep"]
l3 = mymap(update, l1)
print(l3)
