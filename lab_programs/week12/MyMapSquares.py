# 1) 
# a) To find the squares of odd numbers using mymap function, which mimics map.
def square(n):
    return n*n


def myMap(func, list1):
    result = []
    for i in list1:
        result.append(func(i))
    return result


l1 = range(1, 10, 2)
l3 = myMap(square, l1)
print(l3)
