# 5) Write a python program to find the sum of diagonal elements in
# nested 2D list.
list_2D = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sum = 0
for i in range(len(list_2D)):
    sum = sum + list_2D[i][i]
print("Sum:", sum)
