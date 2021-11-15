# 8) Write a program:
# b) that does the following:
# i) shuffle students in class (10 students)
# ii) to choose one student who would become a class rep
# iii) to create a random sample of size 2 from the available number of population who are the potential
# candidates to become event coordinators
# random.sample(x,2)

import random
st = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
a = random.choice(st)
c = random.sample(st, 2)
random.shuffle(st)
print("Shuffled list of students:", st)
print("Class Representative:", a)
print("Possible Event coordinators:", c)
