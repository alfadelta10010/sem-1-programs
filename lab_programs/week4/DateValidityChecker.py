# 4. Check whether a given date is valid. If yes, find the next date. Consider leap year as well.
# (take year, check if leap year, take month no, and set a max date,
# then check if the date entered is between 1 and max date, if yes,
# check if month number is between 1 and 12, if dd == max date and
# month != 12, then dd = 1 and mm +=1, if dd == max date (nested if)
# month = 12, then y+1 as well, else dd+1)
# yy%4 == 0 and (yy%100 != 100 or yy%400 == 0)

dd, mm, yyyy = input("Enter a date (dd/mm/yyyy): ").split("/")
dd = int(dd)
mm = int(mm)
yyyy = int(yyyy)
MaxDD = 0
leap = False
valid = False
days31 = [1, 3, 5, 7, 8, 10, 12]

if yyyy % 4 == 0 and (yyyy % 100 != 100 or yyyy % 400 == 0):
    leap = True
if mm in days31:
    MaxDD = 31
elif mm == 2 and leap:
    MaxDD = 29
elif mm == 2:
    MaxDD = 28
else:
    MaxDD = 30

if dd < 1 or dd > MaxDD or mm < 1 or mm > 12:
    print("Please check the date entered")
else:
    if dd == MaxDD:
        if mm == 12:
            mm = 1
            yyyy = yyyy + 1
            dd = 1
        else:
            mm = mm + 1
            dd = 1
    else:
        dd = dd + 1
    print("The next date is: {}/{}/{}".format(dd, mm, yyyy))

"""
if yyyy % 4 == 0 and (yyyy % 100 != 100 or yyyy % 400 == 0) and mm == 2:
    MaxDD = 29
else:
    if mm % 2 == 0 and mm != 2:
        MaxDD = 30
    elif mm == 2:
        MaxDD = 28
    else:
        MaxDD = 31
"""
