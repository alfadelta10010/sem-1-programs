# WAP to check if the year entered is a leap year

yr = int(input("Enter the year: "))

'''
if yr % 100 == 0:
    if yr % 400 == 0:
        print("{} is a leap year".format(yr))
    else:
        print("{} is not a leap year".format(yr))
else:
    if yr % 4 == 0:
        print("{} is a leap year".format(yr))
    else:
        print("{} is not a leap year".format(yr))
'''

if yr % 4 == 0:
    if yr % 100 != 0 and yr % 400 == 0:
        print("{} is a leap year".format(yr))
    else:
        print("{} is not a leap year".format(yr))
else:
    print("{} is not a leap year".format(yr))
