class Student:
    no_of_holidays = 70
    def __init__(self,aid,asection,asubjects):
        self.id = aid
        self.section = asection
        self.subjects = asubjects

    def printdetails(self):
     return f"Student ID: {self.id} , section is {self.section} and Subjects: {self.subjects}"



class Programmer:
    no_of_holidays = 45

    def __init__(self,id,language):
        self.id = id
        self.language = language

    def printgoo(self):
        return f"Student ID: {self.id} and The Languages are {self.language}  "


class ProStudent(Student,Programmer):
    #no_of_holidays =  100
    pass
angela = ProStudent("20-42186-1",1,["DS,ALGO,WEBTECH"])
Karan = Programmer("20-42187-1",["c++","c#"])

print(angela.printdetails())
print(Karan.no_of_holidays)
print(angela.no_of_holidays)


