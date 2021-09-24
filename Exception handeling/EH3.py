# The finally block, if specified, will be executed regardless if the try block raises an error or not.

# No exception case

x=500

try:
    print(x)
except:
    print("Exception occurred")
finally:
    print("Try except finished")
# Exception Case
print("\n")

try:
    print(z)
except:
    print("Exception occurred")
finally:
    print("Try except finished")
