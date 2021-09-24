set_1 = {"alif","asif"}
set_2 = {"rayied",'fardin',"asif"}
new_set = set_1.intersection(set_2)
print(new_set) #---> intersection

new_set = set_1.union(set_2)
print(new_set)

#Update the required set without duplicate values

set_1.symmetric_difference(set_2)
print("Symmetric difference Update: ",set_1)

# Return a new set but not allowing the different values
new_set = set_1.symmetric_difference(set_2)
print("Symmetric difference: ",new_set)