'''A function is a block of code which only runs when it is called.

You can pass data, known as parameters, into a function.

A function can return data as a result.
'''
def funtionDumb(str):
    "I am A Dumb Function where string is passed and i print it"
    print(str)
    return

funtionDumb("I am A dumb function")
funtionDumb("I am really a dumb and this is called calling where you dumb call me to print")

'''pass by reference and pass by value
All parameters (arguments) in the Python language are passed by reference
'''
def dumbfunction( list ):
    list = ['sudha','maria','hossain']
    list.append(['r'])
    print("Inside the def function :",list)
    return



dumbfunction(list)
list = ['dumb','ass']
print("outside the function : ",list)
