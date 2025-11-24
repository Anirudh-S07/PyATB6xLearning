class MathClass:
    def add(self, a, b):
        return a + b

    # As method overloading is not supported in python if you give a default value to the additional
    # arguments then it can support

    def add(self, a, b, c=10):
        return a + b + c


obj_ref = MathClass()
obj_ref.add(3, 4, 5)
obj_ref.add(3.14, 4.14)
