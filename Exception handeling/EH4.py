# Throw an exception based on condition
# We can throw an exception using `raise` keyword
X= int(input("Enter a positive number: "))

if X <= -1:
    raise Exception("InCorrect number  ")
else:
    print("correct number ",X)