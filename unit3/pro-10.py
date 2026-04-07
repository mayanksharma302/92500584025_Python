class Number:

    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return Number(self.x + other.x)

    def __sub__(self, other):
        return Number(self.x - other.x)

    def display(self):
        print(self.x)


n1 = Number(10)
n2 = Number(5)

a = n1 + n2
s = n1 - n2

a.display()
s.display()
