# 2. Construct dictionary phone_book with:
# Key: number of entries, Values: name, phone number, email,address) and
# perform the following operations:
# a) Add a new number to phone_book
# b) Delete entry from phone book.

phonebook = {}
keys = range(5)
values = [("Hari", 9916345671, "hari@gmail.com", "Bangalore"),
          ("Hamsa", 9916345678, "hamsa@gmail.com", "Bangalore"),
          ("Rahul", 9916345682, "rahul@reddiffmail.com", "Mysore"),
          ("Dhruv", 9916582553, "dhruv@gmail.com", "Bangalore"),
          ("Abhi", 9916880712, "abhi@gmail.com", "Tumkur")]
for i in keys:
    for x in values:
        phonebook[i] = values[i]
print("Phone book dictionary:")
for k in phonebook:
    print(k, ':', phonebook[k])
print("Adding new entry to PhoneBook ⚙")
phonebook[5] = ('Arun', 9916880717, "arun@gmail.com", "Tumkur")
print("The contents of the phonebook after new entry is:")
for k in phonebook:
    print(k, ':', phonebook[k])
key = int(input("Enter the key to delete: "))
del phonebook[key]
print("The phonebook after deletion:")
for k in phonebook:
    print(k, ':', phonebook[k])

