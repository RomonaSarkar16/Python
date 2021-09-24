'''Errors in python -Error in Python can be of two types - Syntax errors and Exceptions. Errors are the problems in a program due to which the program will stop the execution. On the other hand, exceptions are raised when some internal events occur which changes the normal flow of the program. Note: For more information, refer Errors and Exceptions in Python Some of the common Exception Errors are :

IOError : if the file can’t be opened
KeyboardInterrupt : when an unrequired key is pressed by the user
ValueError : when built-in function receives a wrong argument
EOFError : if End-Of-File is hit without reading any data
ImportError : if it is unable to find the module
Type Error : User fault

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else exception runs when there is no exception

The finally block lets you execute code, regardless of the result of the try- and except blocks.

Try Block :

When an error occurs, or exception as we call it,
 Python will normally stop and generate an error message. These exceptions can be handled using the try statement.
 Without try block the programme will crush and raise an error.

Except Block :

When the try block raises an error, the except block will be executed

Else Block: If there isn't any exception,
then this block of code will be executed (consider this as a remedy or a fallback option
if you expect a part of your script to produce an exception).

Finally block :

The finally block, if specified, will be executed regardless if the try block raises an error or not.
Means that The finally block gets executed no matter if the try block raises any errors or not.
.'''
x=20000000000
print(x)

try:
    print(c)
except:
   print("The try block will generate an error, because x is not defined ")