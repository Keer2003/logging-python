try:
    temp=15
    if temp>10:
     print("above ten")
     if temp>20:
         print("And also above 20!")
         
     else:
        print("but not above 20")
except Exception as e:
    print(e)



try:
    temp=15
    if temp>10:
     print("above ten")
     if temp>20:
         pass
         
     else:
        print("but not above 20")
except Exception as e:
    print(e)
