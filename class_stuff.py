# WAP to increment elements of list using callbacks

def f1(l1):
    l2 = []
    for i in l1:
        c1 = i + 1
        l2.append(c1)
    return l2


def sumFunc(q, f2):
    return f2(q)


l = [1, 2, 3]
print(sumFunc(l, f1))

# WAP to print number of characters of file after function reads the given text file
file = open("1.txt", "r")
f = file.read()
c = list(f)
print(len(c))

'''
def size(l):
    with open(l, "r") as f:
        a = f.read()
        print(len(a))

def interface(li, f):
    f(li)
    
interface("1.txt", size)        
'''

# WAP to display a greeting to the new joinees using closure
# WAP to calculate the sum of list of numbers using recursion
# WAP to increment a given number by 5 for n number of times using closure
# WAP to print fibonacci series using recursion up to n
