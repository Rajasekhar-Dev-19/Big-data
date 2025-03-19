"""
--> Class a
--> Object is an physical existence of a class
--> one class can have one or many objects
--> Constructor

--> We have three kind of data members in python OOPS
  --> Instance Variables (Object Level Variables)
  --> Static Variables (Class Level Variables)
  --> Local Variables (Method Level Variables)
  --> Reference variables
--> We have three kind of method in python OOPS
  --> Instance Methods
  --> Class Methods
  --> Static Methods


"""

class Student :
    def __init__(self):
        self.name = 'Python'
        self.age = 30
        self.branch = 'CSE'
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Branch:",self.branch)
s = Student()
s.display()