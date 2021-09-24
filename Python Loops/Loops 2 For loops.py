# List Loooping  ---------------------------------->
print("List :")
print()
newList=["books","Colleen hoover","John Brown","Dean Brown"]
for items in newList:
    print(items)



#continue
# Continue  --------------->
# Skip iteration using `Continue

print("\n Continue : ")
new_list = ["books","Colleen hoover","John Brown","Dean Brown"]
for items in new_list:
    if items == "Dean Brown":
         continue
         print(items) #dean Brown Skipped

    # Break --------->
    # Loop breaker
print("\n Break : ")
new_list = ["books","Colleen hoover","John Brown","Dean Brown"]
for items in new_list:
    if items == "Dean Brown":
         break
         print(items) #dean Brown Skipped


#Looping in `String` --------->
print("\n String index : ")
for i in "Asif Zaman":
    print(items)

########################
# range() function ------------->

# The range() function returns a
# sequence of numbers,starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

print("\nRange function : ")
for i in range(6):
    print(i)

# Step declaring ------------>

print("\nStep : ")
for i in range(1,10,2):
    print(i, end=" ")

# Reverse counting -------------->
print("\nStep reverse : ")
for i in range(10,1,-2):
    print(i,end=" ")