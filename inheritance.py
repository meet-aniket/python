class Person:
  def __init__(self, fName, lName):
    self.firstName = fName
    self.lastName = lName

  def printName(self):
    print(self.firstName, self.lastName)

class Student(Person):
  def __init__(self, fName, lName):
    Person.__init__

object = Student("aniket", "pandey")
object.printName()