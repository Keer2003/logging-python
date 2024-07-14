try:
    temp=input("enter a value:")
    print(temp)
except Exception as e:
    print(e)


try:
    var=int(input("Enter a value:"))
    print(type(var))
    print(var)
    var1=int(input("Enter a variable:"))
    print(var)
    var1=var+var1
    print("enter the value:"+var)
except Exception as e:
    print(e)
