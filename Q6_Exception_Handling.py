try:
    a=int(input("Enter the value"))
    b=int(input("Enter the value"))
    date=eval(input("Enter date"))
    c=a//b
    print("Value of a",a)
    print("Value of b",b)
    print("Value of c",c)

except ArithmeticError as obj:
    print(obj)
except SyntaxError:
    print("Check the date")
except:
    print("Generally Resolved")
else:
    print("Yayyy worked")
finally:
    print("With and without exception")
print("hello")
    

                    
