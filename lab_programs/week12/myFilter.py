# 2) Write a function to mimic filter called myfilter,
# and test it by removing all strings having first
# character as a digit from a given list of strings
def myfilter(func, list1):
    result = []
    for i in list1:
        if func(i):
            result.append(i)
    return result
def xyz(n):
    if not n[0].isdigit():
        return n
    else:
        return None
l1 = ["hi", "hello", "1pes", "2345"]
l2 = myfilter(xyz, l1)
print(l2)
# get rid of the None value
