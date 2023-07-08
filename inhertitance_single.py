# Single Level Inheritance
class Father:
  def __init__(self,p):
    self.p=p
  def disp(self):
    print("Fathers property=",self.p)
class son(Father):
  def __init__(self,p1=0,p=0):
    super().__init__(p)
    self.p1=p1
  def disp(self):
    super().disp()
    print("Property of child=",self.p1+self.p)
s=son(12,10)
s.disp()
