# any condition is given by `IF` keyword

a=10
b=9
if(a<b):
    print("A is bigger ")

# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

a=9
b=9
if a<b:
    print("A is bigger ")
elif a==b:
    print("Similar")

# The else keyword catches anything which isn't caught by the preceding conditions.
a=9
b=1
if a<b:
    print("A is smaller ")
elif a==b:
    print("Similar")
else:
    print("A is bigger ") # All condtioned fail and run else
