# Concept of classes and objects
# WAP in Python to create a class with name, age and marks and print the same
class Student:
    def __init__(self,n,a,m):
        self.n=n
        self.a=a
        self.m=m
    def set_n(self):
        self.n=input("Enter the name")
    def set_a(self):
        self.a=input("Enter the age")
    def set_m(self):
        self.m=input("Enter the marks")
    def get_n(self):
        return self.n
    def get_a(self):
        return self.a
    def get_m(self):
        return self.m    
    def disp(self):
        print("the name=",self.get_n())
        print("the age=",self.get_a())
        print("the marks=",self.get_m())
