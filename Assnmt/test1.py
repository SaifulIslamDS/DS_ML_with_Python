class A:
    def method1(self):
        print("A")

class B(A):
    def method2(self):
        print("B")

class C(B):
    def method3(self):
        print("C")

obj = C()
obj.method1()