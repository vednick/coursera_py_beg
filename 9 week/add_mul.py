from sys import stdin


class Matrix:
    def __init__(self, lst):
        self.lst = [i.copy() for i in lst]

    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.lst])

    def size(self):
        return len(self.lst), len(self.lst[0])

    def __add__(self, other):
        return Matrix(list(map(
            lambda x, y: list(map(lambda z, w: z + w, x, y)),
            self.lst, other.lst)))

    def __mul__(self, other):
        return Matrix([[i * other for i in j] for j in self.lst])

    __rmul__ = __mul__


exec(stdin.read())
