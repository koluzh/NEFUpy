def isnumber(a) -> bool:
    return isinstance(a, int) or isinstance(a, float)


class kek:
    def __init__(self, *args):
        if len(args) != 2:
            raise Exception('invalid arguments')
        self.text = None
        self.num = None
        a = args[0]
        b = args[1]
        if type(a) == str and type(b) == str:
            self.text = a + b
        elif isinstance(a, int) and isinstance(b, int):
            self.num = a + b
        elif isinstance(a, int) and type(b) == str:
            self.num = a
            self.text = b
        elif isinstance(b, int) and type(a) == str:
            self.text = a
            self.num = b

    def show(self):
        print(self.num, self.text)

a = kek('a', 'b')
a.show()
b = kek('a', 1)
b.show()
c = kek(1, 2)
c.show()
d = kek([], 1)
d.show()
