try:
    f=open("hello.txt", "r")
    num=10/0
except FileNotFoundError as e:
    print("error", e)
except ZeroDivisionError:
    print("zerodivision error")
except NegativevalueException:
    print("negative value error")
else:
    pass
finally:
    print("final block")
