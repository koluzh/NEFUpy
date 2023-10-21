class Kek:
    def __init__(self, *args):
        n = len(args)
        list_a = []
        list_b = []
        for i in range(n//2):
            list_a.append(args[i])
        for i in range(n//2, n):
            list_b.append(args[i])
        self.a = list_a
        self.b = list_b

    def __getitem__(self, item):
        if item >= max(len(self.a), len(self.b)):
            raise IndexError
        if item < len(self.b) and item >= len(self.a):
            return self.b[item]
        else:
            return self.b[item] + self.a[item]


lol = Kek(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(lol.a)
print(lol.b)
print(lol[4])
