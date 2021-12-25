# b) Use recursion to raise a number to a given power n
def power(num, toPwr):
    if toPwr == 0:
        return 1
    else:
        return num * power(num, toPwr - 1)


num, po = input("Enter a number raised to a power (2^3): ").split("^")
num = int(num)
po = int(po)
print(power(num, po))
