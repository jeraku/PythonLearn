def div(num:int):
    # return 10/num
    return 10//num

print(div(2))

try:
    print(div(0))
except ZeroDivisionError as e:
    print("zero value error ", e)
except ValueError as e:
    print("value input error ", e)
except Exception as e:
    print("error ", e)
else: 
    print("I am done")
finally:
    print("I am running always")
