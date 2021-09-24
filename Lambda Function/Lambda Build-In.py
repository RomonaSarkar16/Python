'''
Map() ->
 The map() function in Python takes in a function and a list.
 The function is called with all the items in the list and a new list is returned which contains items
  returned by that function for each item.

  map() ->

-->takes function and list as argument
-->return a new list based on the function evaluation
SYNTAX--
# map() ->
#newList=list(map(lambda -----),listName)

#Differance between map() and filter() ->

# In map: Function will be applied to all objects of iterable.

# In filter: Function will be applied to only those objects of iterable who goes True on the condition specified in expression.
'''
my_list = [12,34,54,6,77,12,23,45]
newList = list(map(lambda z : z*2,my_list))  # funtions runs for every objects of the iterable
print("Double Numbers : ",newList)

'''
Filter() -> The filter() function in Python takes in a function and a list as arguments. The function is called
 with all the items in the list and a new list is returned which contains items for which the function evaluates to True.
 filter() ->

-->takes function and list as argument
-->return a new list based on the function evaluation
#Syntax ---->
# newList=list(filter(lambda ---- ),listName)

In map: Function will be applied to all objects of iterable.
In filter: Function will be applied to only those objects of iterable who goes True on the condition specified in expression. 

'''
random_list1 = [200,300,12,3,4,5,6,7,8,90]
newList = list(filter(lambda x: x%2==0,random_list1))
print("Print only even numbers :",newList)

newList = list(filter(lambda x: x%2!=0,random_list1))
print("Print only odd numbers :",newList)
print("\n")
newList = list(filter(lambda x: x*3,random_list1))
print("Function will be applied to only those objects of iterable who goes True on the condition specified in expression.\nSo NO Changes Showed ")
print("Print only even numbers :",newList)