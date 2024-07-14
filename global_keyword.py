try:
    def myfun():
        global temp
        temp="fantastic"
    myfun()
    print("python is:"+temp)
except Exception as e:
    print(e)
        
