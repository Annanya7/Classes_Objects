from prog2_variables import Sample
# Instance variable outside the class is called via the object of the class 
s=Sample()
s.modify()
s1=Sample()
print("First object value=",s.x)
print("Second object value=",s1.x)
