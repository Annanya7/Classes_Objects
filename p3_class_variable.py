# Understanding a class variable
class Holder:
    x=10
    @classmethod
    def modify(cls):
        cls.x+=100
