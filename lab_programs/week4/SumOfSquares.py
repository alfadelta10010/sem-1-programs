# 1. WAP which uses a while loop to sum the squares of integers (starting from 1) until the total exceeds 200.
# Print the final total and the last number to be squared and added.
num = 0
total = 0
while total < 200:
    num = num + 1
    total = total + num ** 2
print("Total:", total)
print("Last number:", num)
