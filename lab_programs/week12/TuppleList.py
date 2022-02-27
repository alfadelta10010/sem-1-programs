# 1) c) To create a list of tuples
def xyz(n):
    return n, len(n)
def mymap(func, list1):
    result = []
    for i in list1:
        result.append(func(i))
    return result
l1 = ["walk", "eat", "sleep"]
l3 = mymap(xyz, l1)
print(l3)
