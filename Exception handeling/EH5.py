X = int(input("X is:"))
Y = int(input("Y is:"))
try:
   X/Y
except(ZeroDivisionError):
    print("Exception: Check the value of y")
else:
    print(X/Y)