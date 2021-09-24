class Student:
    no_of_holidays = 70
    def __init__(self,aid,asection,asubjects):
        self.id = aid
        self.section = asection
        self.subjects = asubjects

    def printdetails(self):
     return f"Student ID: {self.id} , section is {self.section} and Subjects: {self.subjects}"

    @classmethod
    def change_num_of_holidays(cls,new_holidays):
        cls.change_num_of_holidays=new_holidays

    @classmethod
    def from_dash(cls, string):
      return cls(*string.split("-"))

    @staticmethod
    def printanythiny():
        print("SINGLE INHERITANCE IS ONGOING")


class Programmer(Student):
    no_of_holidays = 45

    def __init__(self,aid,asection,asubjects,language):
        self.id = aid
        self.section = asection
        self.subjects = asubjects
        self.language = language

    def printgoo(self):
        return f"Student ID: {self.id} , section is {self.section} , subjects are {self.subjects} and The Languages are {self.language}  "

karan = Student("20421861",121,["Data Structure,Algorithm"])

angela = Programmer("20-42186-1",121,"Data Structure,C#",["python","c#"])

print(karan.printdetails())
print(angela.printgoo())



