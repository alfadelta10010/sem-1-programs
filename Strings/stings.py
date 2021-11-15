a = "Hello"
print(a.find("ell"))  # 1 cause index 1 has the letter e
print(a.replace("o", "oooo"))
print(len(a))
print(min(a))
print(max(a))
Concat = '+'
repeat = '*'
a = a + " world"
print(a)
print()

# format methods
name = "Rohith"
# using %
print("hello %s" % name)
# using .format()
print("hello {}".format(name))
# using fstring
print(f"hello {name}")

print(a.endswith("o"))

b = ["hello", "there", "general", "Kenobi", "you", "are", "a", "bold", "one"]
sentence = ""
for i in b:
    sentence = sentence + i + " "
print(sentence)

sentence2 = "\n".join(b)
print(sentence2)
