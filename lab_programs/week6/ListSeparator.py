# 3) Given a heterogeneous list, create separate lists
# for different types of data. Write a python program to achieve the same.
l = ['facebook', {23, 89}, {8.4, 9.3}, "twitter", 25, 90, "whatsapp", 55, 44,
     ("p", "e", "s"), 45, 0.9, 9.5, 2, 150, (78, 56), [45, 90, 23],
     ["pesuacademy", "pes"]]
l_int = []; l_float = []; l_str = []; l_tuple = []; l_list = []; l_set = []
for i in l:
    if type(i) == int:
        l_int.append(i)
    if type(i) == float:
        l_float.append(i)
    if type(i) == str:
        l_str.append(i)
    if type(i) == tuple:
        l_tuple.append(i)
    if type(i) == list:
        l_list.append(i)
    if type(i) == set:
        l_set.append(i)
print("Integer list:", l_int)
print("Float list:", l_float)
print("String list:", l_str)
print("Tuple list:", l_tuple)
print("List's list:", l_list)
print("Set list:", l_set)
