class Ball:
    def __init__(self):
        self.pos = 1

    def move(self, letter: str):
        if 'A' in letter:
            self.A()
        if 'B' in letter:
            self.B()
        if 'C' in letter:
            self.C()

    def A(self):
        if self.pos == 1:
            self.pos = 2
        if self.pos == 2:
            self.pos = 1

    def B(self):
        if self.pos == 3:
            self.pos = 2
        if self.pos == 2:
            self.pos = 3

    def C(self):
        if self.pos == 1:
            self.pos = 3
        if self.pos == 3:
            self.pos = 1


b = Ball()
kek = str(input())
for c in kek:
    b.move(c)

print(b.pos)
