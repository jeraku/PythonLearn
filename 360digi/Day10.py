"""
default argument
*args
**Kwargs

# finite loop is for loop
# and infinite loop is while loop

"""
n=6
k=n+1

for i in range(0,n):
    for j in range(0,k):
        print(" ", end="")
    k=k-1
    for j in range(0,i+1):
        print("* ", end="")
    print("\r")

# to perfrom non mandatory param
def say(message, times=2):
    print(message*times)
say("heello")
say("heello ",6 )

def func(*args):
    print(type(args))
    for arg in args:
        print(arg)
    
func("heelos ", "mr", "jegan")

def func1(**args):
    print(type(args))
    for arg, val in args.items():
        print(arg, val )
    
func1(word="heelos ", title= "mr", name="jegan")

def funcs(val, *args, **kargv):
    print(val)
    # for arg in args:
    #     print(arg)
    for k,v in kargv.items():
        print(f"k {k} and v is {v}", end="")

funcs(1,4,43,45,3,234,56,7,47, name="jegan", title="Mr", word = "ello")