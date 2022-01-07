lis = ["hi", "1gff", "h3445", "6sds", "dfg", "234234"]
print(list(filter(lambda x: x if x[0].isdigit() is False else None, lis)))
