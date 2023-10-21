def isnumber(a) -> bool:
    return isinstance(a, int) or isinstance(a, float)


class Nums:
    def __init__(self, kek: list):
        self.nums = []
        for i in kek:
            if isnumber(i):
                self.nums.append(i)

    def mean(self):
        m = 0
        for i in self.nums:
            m += i
        return m / len(self.nums)

    def show(self):
        print(self.nums)

l = [[], 'a', {'a': 123}, 123, 1.23]

a = Nums(l)
a.show()
print(a.mean())