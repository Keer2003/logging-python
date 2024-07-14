try:
    temp="elegent"
    def myfun():
        temp="funtastic"
        print("python is" + temp)
    myfun()
    print("python is" + temp)
except Exception as e:
    print(e)
