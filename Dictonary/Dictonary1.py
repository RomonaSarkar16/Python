#dictonary is notjimg but a key of pair values
dic1 ={"Angela": "Beef","Omi":"Chicken","Veronica":"Fish","Philip": "Pig"}
dic2 ={"Sudha" : {"Breakfast" : "Roti","Lunch" : "Chicken biriyani","Dinner": "Beef "}}
#dic = ()
#dicc ={}
#diccc = []
#print(type(dic))

print(dic1)
print(dic1["Omi"])
print(dic2["Sudha"])
print(dic2["Sudha"]["Breakfast"])

print(dic1["Angela"])

#updating values

dic1["ovi"] = "Juck food"
print(dic1)
dic1["3000"] = "Jul puri"
print(dic1)

#deleting a value

del dic1["3000"]
print(dic1)

#copy a dict
d3 = dic1.copy()
del d3["ovi"]
print(d3)

#get function in dict
print(dic1.get("Angela"))
dic1.update({"lELA ": "mEATBALL"})
print(dic1)

#print only keys
print(dic1.keys())
#print only items
print(dic1.items())
#delete all values

dic1.clear()
print(dic1)

#del dic1
#print(dic1)



