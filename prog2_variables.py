# We are gonna practise the types of variables- instance and class variables
# Create and increment an instance variable
class Sample:
    def __init__(self):
        # The variable inside a class with a self keyword: Instance
        self.x=100
    def modify(self):
        self.x+=100
