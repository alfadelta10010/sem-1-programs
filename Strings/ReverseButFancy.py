# WAP to reverse a string, but fancy
def reverse1(s):
    return s[::-1]


def reverse2(s):
    rev = ""
    i = len(s)
    while i > 0:
        rev = rev + s[i-1]
        i = i - 1
    return rev


print(reverse1(input("string entry: ")))
print(reverse2(input("string entry: ")))
print(reverse2("qwerty reversed is " + reverse2("qwerty")))
# Added ReverseButFancy and modified ReverseString.py and functions.py, deleted files.py
