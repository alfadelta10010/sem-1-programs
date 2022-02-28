# 3) Write a function that iterates over a list. The list needs to iterate over
# 20 numbers, but the the list is made from user input, and might not have 20
# numbers in it. After you reach the end of the list, you just want the rest
# of the numbers to be interpreted as 0.
def number(inNum):
    print(inNum, end=" ")


def iterate(lis):
    for it in range(20):
        try:
            number(lis[i])
        except IndexError:
            number(0)


l1 = []
i = 0
while i <= 20:
    n = input("Enter number: ")
    if n == "*":
        break
    l1.append(int(n))
    i = i + 1
iterate(l1)
