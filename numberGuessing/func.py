# global variable
var2 = 1  # global scope

def func():
    var2 = 2  # local scope
    print('local var:', var2)
func()
print('global var:', var2)