def  my_function(a,b):
   return 2*(a+b)
print(my_function(22,33))

lambda_function = lambda f,y : 2*(f+y)
print(lambda_function(22,66))

'''
while using def, we needed to define a function with a name cube and needed to pass a value to it.
After execution, we also needed to return the result from where the function was called using the return keyword.

Lambda definition does not include a “return” statement, 
it always contains an expression that is returned. We can also put a lambda definition anywhere a function is expected, and
 we don’t have to assign it to a variable at all. 
This is the simplicity of lambda functions
'''