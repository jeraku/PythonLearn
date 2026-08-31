from datetime import datetime

# Below piece of code is a simple time display function.
def print_time():
    #Before logic
    time = datetime.now()
    #after logic
    return time
print(print_time())

# Decorator Ex:

def log_it(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

print("---------------")
#Adding additional logic using decorator.
@log_it
def print_time_decorator():
    print(datetime.now())
print_time_decorator()