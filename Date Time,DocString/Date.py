#display the current date
import datetime
x = datetime.datetime.now()
print(x)

#return the year and name of the week
print(x.year)
#print(x.strftime("%A"))

X= datetime.datetime(2021,7,22,12,56)
print("The weekday of the input year,month and date :",X.strftime("%A"))
print("The century of the input year,month and date :",X.strftime("%C"))
print("The date of the input :",X.strftime("%x"))
print("Daytime :",X.strftime("%p"))