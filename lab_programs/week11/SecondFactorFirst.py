# 2) c) Given a list of tuples containing two integers, remove all tuples
# where second element in tuple is not a factor of first element
li = [(2, 3), (4, 2), (6, 3), (6, 4), (16, 4), (5, 2)]
print(list(filter(lambda x: x if x[0] % x[1] == 0 else None, li)))
