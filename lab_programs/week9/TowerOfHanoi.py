# 3 a) Solve Tower of Hanoi
def towerOfHanoi(n, from1, to, aux):
    if n == 1:
        print("Move ring 1 from", from1, "peg to", to, "peg")
        return
    towerOfHanoi(n-1, from1, aux, to)
    print("Move ring", n, "from", from1, "peg to", to, "peg")
    towerOfHanoi(n-1, aux, to, from1)


num = int(input("Enter number of discs: "))
towerOfHanoi(num, "Left", "Right", "Middle")
