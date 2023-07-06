from p3_class_variable import Holder
h=Holder()
print("Instance Varible beforr class modified it",h.x)
print("class Varible beforr class modified it",Holder.x)
h.modify()
print("Class variable",Holder.x)
print("Instance Varible after class modified it",h.x)
