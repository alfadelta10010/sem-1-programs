# WAP to check if the year entered is a leap year

yr = int(input("Enter the year: "))


if yr % 4 == 0:
    if yr % 100 != 0 or yr % 400 == 0:
        print("{} is a leap year".format(yr))
    else:
        print("{} is not a leap year".format(yr))
else:
    print("{} is not a leap year".format(yr))
