class Person:
  '''
  Self parameter is a reference to the current instance of the class, 
  and is used to access variables that belong to the class.

  Self parameter is a reference to the current instance of the class,
   and is used to access variables that belong to the class and it does not
  have to be named self, we can name it whatever we want. but it has to be 
  the first parameter of any function in the class.
  '''
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def printName(self):
    print('Hello my name is: ', self.name)

obj1 = Person("Amit", 20)
obj1.name = "Aniket Pandey"

''' del statement is used to delete object and its properties '''
# del obj1.name
# del obj1

''' 
Class statement can not empty, but if we want to crate class definition with no
content we will put pass statement to avoid getting an error.
'''
class Person:
  pass

object = Person()