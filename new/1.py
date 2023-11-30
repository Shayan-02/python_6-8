class A:
    def info2(self):
        print("Class A")


class B:
    def info(self):
        print("Class B")


class C(A, B):
    pass


my_instance = C()
my_instance.info()


