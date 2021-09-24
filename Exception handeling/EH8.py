#LookUp Error
# Lookup Error acts as a base class for the exceptions that occur when a key or index used on a mapping or sequence of
# a list/dictionary is invalid or does not exists.
dictonary =["1.crybaby","2.Mrs. potato Head","3.trainning wheels"]
try:
    print(dictonary[1])
except LookupError:
    print("out of bounds")
else:
    print(dictonary[1])
print("\n")
list1 = ["Angela",
         "Rayied",
         "Omi",
         "hubert"]
try:
    print(list1[7])
except LookupError:
    print("out of bounds")
else:
    print(list1[1])
