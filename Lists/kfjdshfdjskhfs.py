# WAP to perform the following operation using given list as input
l = eval(input("enter a list"))
for i in l:
    if i.isalpha() == True:
        print(i)
    elif i.isdigit()==True:
        print(i)
