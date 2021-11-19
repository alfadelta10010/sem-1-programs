# 8. WAP that reads two integer values n and m from the user and then produces a box that is n wide and m deep.
# n = columns, m = rows
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))
i = 0
while i < m:
    j = 0
    while j < n:
        if i == 0 or i == m - 1 or j == 0 or j == n - 1:
            print('@', end=' ')
        else:
            print(' ', end=' ')
        j = j + 1
    i = i + 1
    print()
