# The concept of Inheritance: Here, we pass the class in the parameter of another class , so that the dervied class can use the base class method using its own object and hence can accesss the functions of the same
from teacher import Teacher
class Student(Teacher):
    def set_marks(self,m):
        self.m=m
    def get_marks(self):
        return self.m
# Can we create  a display function here ?
s=Student()
s.set_id(100)
s.set_name('Monika')
s.set_salary(100000000000)
s.set_marks(98)
print("The student id=",s.get_id())
print("The student name=",s.get_name())
print("The student salary=",s.get_salary())
print("The student marks=",s.get_marks())
