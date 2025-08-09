# overriding

class A:
    class_var_1 = "I am in class A class variable"

    def __init__(self):
        self.var1 = "I am in class A instance Var"
        self.class_var_1 = "I am in class A instance Var"
        # self.special = "I am special"

    def abc(self):
        print("I am class A")


class B(A):
    class_var_2 = "I am in class B class variable"

    def __init__(self):  # overwriting the A constructor
        super().__init__()
        self.var1 = "I am in class B instance Var"
        self.class_var_1 = "I am in class B instance Var"

    def abc(self):
        print("I am class B")


a = A()
b = B()

print(b.class_var_1)
# it checks if there is an instance var in B.if not , then checks if there is an instance variable in A,
# if not, then checks class var in B, if not, then in class var A

# overriding constructor
# if i write constructor in B, hten A constructor gets override
# to have A and B both constructor
