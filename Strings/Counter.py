# WAP to count all the letters, digits and special symbols from a given string
s2 = "fghTYTAsFfdGHG!*83213&*87"
alphaCount = 0
numCount = 0
specCount = 0
for i in s2:
    if i.isalpha():
        alphaCount = alphaCount + 1
    elif i.isdigit():
        numCount = numCount + 1
    else:
        specCount = specCount + 1
print("alphabets: {}, numbers: {}, spec: {}".format(alphaCount, numCount, specCount))
