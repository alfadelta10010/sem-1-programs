# 7) Write a python program to clear the right most set bit of a number. (flip it too)

n = int(input("Enter a number: "))
ans = n & (n - 1)
print("The number, when the right most set bit is cleared, becomes:", ans)
