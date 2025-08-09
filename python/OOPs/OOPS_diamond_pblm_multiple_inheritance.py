
class A:
    def met(self):
        print("inside class A")


class B(A):
    def met(self):
        print("inside class B")


class C(A):
    def met(self):
        print("inside class C")


class D(B,C):
    def met(self):
        print("inside class D")


a = A()
b = B()
c = C()
d = D()

d.met()