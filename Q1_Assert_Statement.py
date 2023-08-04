# Exception Handing
try:
    x=int(input("Enter a number between 5 and 10"))
    assert x>=5 and x<=10
    print("The number=",x)
except:
    print("The condition is not fulfilled")
