# compute cube of number using command line argument
import sys
import math

q = int(sys.argv[1])  # index 0 is the file name
c = q ** 3
print("Using operators:", c)

# using math
c = math.pow(q, 3)
print("Using Math Library:", c)
