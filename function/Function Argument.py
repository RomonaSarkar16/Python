'''
The terms parameter and argument can be used for the same thing: information that are passed into a function.

WE CAN CALL A FUNCTION WITH THESE ARGUMENTS_
Required arguments
Keyword arguments
Default arguments
Variable-length arguments
'''

#REQUIRED ARGUMENTS : this function expects 2 arguments and gets 2 arguments
def myfunction_Require(name,age):
    "prints the arguments/parameters when it is called with 2 arguments. No Less NO More"
    print("My name is ",name + "\n" "and my age is",age )

myfunction_Require(name='Angela',age='21')
print("\n")
#KEYWORD ARGUMENTS
def myfunction_Keyword(friend1,friend2,friend3):
    "argument order doesnt matter"
    print("My friends are soooo good they are "+ friend1,",",friend2,"and", friend3)
myfunction_Keyword(friend3="alif",friend1="rayied",friend2="asif")
print("\n")
#Default arguments
def mycountry(country_name ="Bangladesh"):
    print(" i am from ", country_name)
mycountry("Norway")
mycountry("america")
mycountry("Spain")
print("\n")
#passing list as arguments

def foodIlike(myfood):
    for x in myfood:
        print(x)

foods =["biriyani","coke","cake"]
foodIlike(foods)
print("\n")
#function return values

def mymath(x1):
    return 12 * x1
print("return value returns : ", mymath(2))
print("return value returns : ", mymath(12))
print("return value returns : ", mymath(22))

print("\n")

def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement

print("\n")

