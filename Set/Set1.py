Set1 = set()
#print(type(Set1))
Set2 = set([100,200,300])
print(Set2)
print(type(Set2))

#python set is unordered and immutable
#items can not be changed but items can be removed or be added
#Duplicates values are not allowed

set = {"book","study","naruto","life",True,"life"}

print("Dublicates not allowed :",set)

set.add(12)
print("after adding :",set)

s1 = set.union({10,2,3})
print("after union : ",set,s1)
print("\n")
print("lets see what s1 has inside of it: ",s1)

s2 = {12,45,6}
print("S2: ",s2)
s1 = set.intersection(s2)
print("after intersection of s1 and s2: ",s1)

print("set and s2 has no common:",set.isdisjoint(s2)) #gives false if has a common value
set.remove(12)
print("after removing 12  :",set)
"""there are also more methods in set function
Method ---------------------------- Do

add()	                         Adds an element to the set
clear()      	                 Removes all the elements from the set
copy()	                         Returns a copy of the set
difference()	                 Returns a set containing the difference between two or more sets
difference_update()              Removes the items in this set that are also included in another, specified set
discard()	                     Remove the specified item
intersection()      	         Returns a set, that is the intersection of two other sets
intersection_update()	         Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	                 Returns whether two sets have a intersection or not
issubset()                    	 Returns whether another set contains this set or not
issuperset()                  	 Returns whether this set contains another set or not
pop()               	         Removes an element from the set
remove()            	         Removes the specified element
symmetric_difference()	         Returns a set with the symmetric differences of two sets
symmetric_difference_update()	 inserts the symmetric differences from this set and another
union()             	         Return a set containing the union of sets
update()	                     Update the set with the union of this set and others
"""

