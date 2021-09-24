'''
While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.
anonymous functions are also called lambda functions.
lambda arguments : expression

A lambda function can take any number of arguments, but can only have one expression.
The expression is evaluated and returned.

WHY USE LAMBDA FUNCTION?
We use lambda functions when we require a nameless function for a short period of time.

'''

y = lambda r,t,s : r * t * s
print(y(3,4,5))

#as a string
x = "Angela Will Start Reading Books Again"
(lambda x : print(x))(x)

#The power of lambda is better shown when you use them as an anonymous function inside another function.
def my_baby(n):
    return lambda a : a * n

my_tripler = my_baby(3)
my_doubler = my_baby(2)
print(my_tripler(33))
print(my_doubler(22))
############################
def my_fun(x):
    return lambda z: z*x
Answer_1 = my_fun(3)
Answer_2 = my_fun(5)
print("Answer 1 : ",Answer_1(4))
print("Answer 2 :", Answer_2(5))