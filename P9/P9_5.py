class Kek:
    def __init__(self, a: list):
        self.a = a

    def __getitem__(self, index):
        if index >= len(self.a):
            return 0
        return self.a[index]

    def __add__(self, other: 'Kek'):
        res = []
        for i in range(max(len(other.a), len(self.a))):
            res.append(self[i] + other[i])
        return res


a = Kek([1, 2, 3, 4, 5])
b = Kek([1, 2, 3])
c = a + b
print(c)