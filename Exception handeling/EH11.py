#type error
age = ""
if not type(age) is int:
    raise TypeError("Please enter the integer number")
else:
    print(age)