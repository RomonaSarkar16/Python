#for loops
#list1 =["angela","hridy","ramisa","momo"]
list1 =[["angela",1],["hridy",2],["ramisa",3],["momo",4]]
dict1 = dict(list1)
print(dict1)
#in here you will see the keys and values alltogether in output
for i,t in dict1.items():
 print(i,"placed ",t)
#in here you will only see the keys because the item is only being printed
for item in dict1:
  print(item)

############
list3= ["angela",45,6,78,200,True,65,1,234,5,6,int , float]
for items in list3 :
 if (items==int) | (6<=items):
  print("integer numbers are :",items)
else:
 print("Blank")


