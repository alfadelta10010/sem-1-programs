''''
Exception Handling:
Exception: A python object that simply represents error
Types of Error:
1) Syntax/Compile Error
2) Logical Error
3) Runtime Error
'''


a = 4
b = 0
Try:
	print(a/b)
Except Exception:
	print("you cannot divide any number by 0")
print("End")