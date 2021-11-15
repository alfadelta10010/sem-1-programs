# 10) Generate the same random number every time.
import random
random.seed(5)
a = random.random()
random.seed(5)
b = random.random()
print("First no. is {} and second is {}".format(a, b))
