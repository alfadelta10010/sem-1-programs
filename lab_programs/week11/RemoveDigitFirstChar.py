# 2. WAP using map/reduce/filter and lambda
# a) Given a list of strings,remove all strings that have first character as a digit
lis = ["hi", "1gff", "h3445", "6sds", "dfg", "234234"]
print(list(filter(lambda x: x if x[0].isdigit() is False else None, lis)))
