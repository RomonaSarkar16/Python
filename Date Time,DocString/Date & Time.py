import time
ticks = time.time()
print("Number of ticks from 1 january, 1970: ",ticks)
print("\n")
localtime = time.localtime(time.time())
print("The just local time : ",localtime)

print("\n")

asctime = time.asctime(time.localtime(time.time()))
print("The readable time is : ",asctime)


###t − This is a tuple of 9 elements or struct_time representing a time as returned by gmtime() or localtime() function

t= time.localtime()
print("time.asctime(t) : %s"% time.asctime(t))