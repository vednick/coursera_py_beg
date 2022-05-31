from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


class Matrix:
    def __init__(self, lst):
        self.lst = [i.copy() for i in lst]

    def __str__(self):
        return "\n".join(["\t".join(map(str, i)) for i in self.lst])

    def size(self):
        return len(self.lst), len(self.lst[0])

    def __add__(self, other):
        if len(self.lst) == len(other.lst):
            return Matrix(list(map(
                lambda x, y: list(map(lambda z, w: z + w, x, y)),
                self.lst, other.lst)))
        else:
            raise MatrixError(self, other)

    def __mul__(self, other):
        return Matrix([[i * other for i in j] for j in self.lst])

    __rmul__ = __mul__

    def transpose(self):
        mm = Matrix([[] for _ in range(len(self.lst[0]))])
        for i in range(len(self.lst[0])):
            for j in range(len(self.lst)):
                mm.lst[i].append(self.lst[j][i])
        self.lst = [i for i in mm.lst]
        return Matrix(self.lst)

    @staticmethod
    def transposed(a):
        mm = [[] for _ in range(len(a.lst[0]))]
        for i in range(len(a.lst[0])):
            for j in range(len(a.lst)):
                mm[i].append(a.lst[j][i])
        return Matrix(mm)


exec(stdin.read())


# class MatrixError(BaseException):
#     def __init__(self, matrix1, matrix2):
#             self.matrix1 = matrix1
#             self.matrix2 = matrix2
#
#
# class Matrix:
#     def __init__(self, lst):
#         self.lst = deepcopy(lst)
#
#     def __str__(self):
#         return '\n'.join(['\t'.join(map(str, line)) for line in self.lst])
#
#     def size(self):
#         return len(self.lst), len(self.lst[0])
#
#     def __add__(self, other):
#         if self.size() == other.size():
#             arr = []
#             for row in range(len(self.lst)):
#                 arr.append([*map(sum, zip(self.lst[row], other.lst[row]))])
#             return Matrix(arr)
#         else:
#             raise MatrixError(self, other)
#
#     def transpose(self):
#         self.lst = list(zip(*self.lst))
#         return Matrix(self.lst)
#
#     @staticmethod
#     def transposed(other):
#         return Matrix(list(zip(*other.lst)))
#
#     def __mul__(self, alpha):
#         arr = []
#         for line in self.lst:
#             arr.append([*map(lambda x: x * alpha, line)])
#         return Matrix(arr)
#
#     __rmul__ = __mul__
#
#
# exec(stdin.read())
