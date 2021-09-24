 #declaring global variable

string1 = 'Canada'

def decision1():
    string1 = 'USA'
print(" I am in love with ",string1)

decision1()
print("i love",string1) #printing global

#global variable
def decision2():
   global string2
   string2 ='Bangladesh'

decision2()                      #defined string3 globally
print("i will always love ",string2)

def function3():

    global string4
    string4 = 'Canada'

function3()
print("Angela Sarkar wants to live in ", string4)