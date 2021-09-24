#add() and update() are used to add the items in `Set`

#Add method ------------------------>

# add() is used to add a single item in Set :

set1={"A","Tom","Pro","O","J","M"}
set1.add("Sad")
print("Single item addition : ",set1)

#Update() is used to add multiple items like (List, Tuples, Dict)

#Set to Set addition-->

set1={"As","Tom","Pro","Ov","Mi"}
set2={1,55,67,89.0}

set1.update(set2)
print("Set Set add : ",set1)

#Set to List addition-->

set1={"Asif","Tamim","Protty","Ovy","Jubayer","Mim"}
list1=[1,90,89+2j]
set1.update(list1)
print("Set List add : ",set1)

# 1 Using Remove() ------>
# >>>> Remove() will show an `ERROR` when the item we want to remove that doesn't exist in the SET <<<<<

set1={"Angela","Sudha","Shuchi","Oishi","Afrin"}
set1.remove("Afrin")
print("afrin Removed : ",set1)

# 2 Using Discard() -------->
# >>>> Discard() will not show an `ERROR` when the item we want to remove that doesn't exist in the SET <<<<<

set1={"Angela","Sudha","Shuchi","Oishi","Afrin"}
set1.discard("Afrin")
print("\nAfrin Removed  : ",set1)

# 3 Using Pop() -------->
# >>>>> Pop() will remove the last element of the `Set` as Set is inordered so we dont know what is the last item <<<<<

set1={"Angela","Sudha","Shuchi","Oishi","Afrin"}
set1.pop()
print("\nLast item removed : ",set1)


# 4 Using Clear() --------->
# >>>>> Clear will remove all the elements of the set but set remains <<<<<

set1={"Angela","Sudha","Shuchi","Oishi","Afrin"}
set1.clear()
print("\nSet is blank : ",set1)

# 5 Using del() ----->
#set1 will be removed from the memory (No existance)
set1={"Angela","Sudha","Shuchi","Oishi","Afrin"}
del set1