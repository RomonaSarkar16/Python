#program to see the eligibility of a student whether she is allowed to sit in the xm
#author hridy

#input

classno_hd = int(input("number of classes were held :"))

attendance = int(input("number of classes attended by student :"))


percentage = (attendance/classno_hd)*100
print("total percentage of the student",percentage,"%")

if percentage <75:
    print("yes")
else:
    print("no")
