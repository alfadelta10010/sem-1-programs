def counter():
    count = 0
    def incrementcount():
        n=int(input("enter a number"))
              
        nonlocal count
        count += 5
        return count
    return incrementcount
