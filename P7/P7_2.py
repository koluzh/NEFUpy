class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        print(self.a, self.b)

A = MyClass(1, 2)
A.show()

B = MyClass('2', 'a')
B.show()
