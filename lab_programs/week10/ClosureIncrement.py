# Increment a given number by 5 for n number of times using closure
def counter(count):

    def incrementCount():
        nonlocal count
        count = count + 5
        return count

    return incrementCount()


n = int(input("Enter a number: "))
print(n, "+ 5 =", counter(n))
