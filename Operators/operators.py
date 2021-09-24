
# in / not in / is not operators are used to check the items in list
# in and not in used in list or string
# is not is use in no literal object

#Character check in string

name = "Romona Magdalene Sarkar"
input22 = input("enter the letter to be found: ")
if input22 in name:

    print("The string is found")
else:
    print("Error string")

#List item check
friend_list=["Angela","Ramisa","sudha","Omi"]

if "Angela" in friend_list:
    print("\nAvailable")
else:
    print("Angela not available")

if "omi" not in friend_list:
    print("\nNo avalilable")
else:
    print("Available")


# `is not`

name=None
if name is not  None:
    print("Name is {}".format(name))
else:
    print("\nNo name available")