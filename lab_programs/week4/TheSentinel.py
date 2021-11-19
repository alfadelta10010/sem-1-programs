# WAP to which averages positive integers. your program should prompt the user to enter
# integers until the user enters a negative integer.

a = []
i = 0
while True:
    n = int(input("Enter number: "))
    if n < 0:
        break
    a.append(n)
    i = i + 1
avg = float(sum(a)/len(a))
print("The average is:", avg)
