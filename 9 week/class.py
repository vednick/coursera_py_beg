from sys import stdin


class Matrix:
    def __init__(self, lst):
        self.lst = [i.copy() for i in lst]

    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.lst])

    def size(self):
        return len(self.lst), len(self.lst[0])


exec(stdin.read())
