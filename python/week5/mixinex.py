"""
mixin  - design pattern for inheritance
mixin is additional support for a class
each mixin will have one job at a time
does not have __init__ method so we can differentiate.

"""
# from 
class MixinLogin():
    def log(self,message: str):
        print("Log here ", message)

# import datetime
from datetime import time
class TimeStampex():
    def now():
        return time.datetime

