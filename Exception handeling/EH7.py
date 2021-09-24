#attribute error
# When a non-existent attribute is referenced, and when that attribute reference or assignment fails, an attribute error is raised.
def random():
    c =20

    print("c :",c)
try:
    object1 = random()

    print(object1.attribute) # there is no `attribute` Attribute  in random() function
except AttributeError:
    print("Attribute exception occured")
else:
    print("No exception occured")