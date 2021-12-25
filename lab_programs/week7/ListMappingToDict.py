# 6. Write a Python Program to construct two  lists namely, college names
# and ranking and map the same lists into dictionary.
# if its wrong, why does it feel so right?

college_name = []; ranking = []
n = int(input("Enter number of elements for dictionary: "))
print("For keys:")
for x in range(0, n):
    element = input("Enter college name: ")
    college_name.append(element)
print("For values:")
for x in range(0, n):
    element = int(input("Enter rank " + str(x + 1) + ": "))
    ranking.append(element)
college_pos_rate = dict(zip(college_name, ranking))
print("The dictionary is: ")
for key in college_pos_rate:
    print(key, ':', college_pos_rate[key])

'''
Enter number of elements for dictionary: 3
For keys:
Enter college name: PES
Enter college name: SRM
Enter college name: SSN
For values:
Enter rank 1: 1
Enter rank 2: 3
Enter rank 3: 2
The dictionary is: 
PES : 1
SRM : 3
SSN : 2
'''