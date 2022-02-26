# Find Nth root of a number using closure
def findNRoot(inP):
    def root(x):
        return x ** (1/inP)
    return root


n = int(input("Enter Nth Root: "))
inner = findNRoot(n)
num = int(input("Enter a number: "))
print("The root is:", inner(num), "\nor ({})^{} = {}".format(inner(num), n, num))
