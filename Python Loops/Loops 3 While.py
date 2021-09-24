# Sytax -------------->

#------------------------------
# Counter initialiazation
# while(Condition):
#     Step
#     Increament/Decreament
#Loop Closed
#------------------------------
print("Introduction to while")

i=1
while (i<=5):
 print(i)
i+=1


#`Break` keyword is used to break the loop even if the condition true -------->

print("\nBreak in while : ")
i=1
while i<6:
    print(i)
    if i==3:
        break
    i+=1
# `Continue` is used to stop the current iteration---------->


print("\n Continue in while : ")
i=0
while i<6:
    i+=1
    if i==3: # 3 is not printed
        continue
    print(i)

# Note :  In do while or while loop Counter Increament or decreament must be declared before continue
