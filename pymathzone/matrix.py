from .utils.matrix import *


class Matrix:
    def __init__(self, rows: int, cols: int, data=None):
        """
        :param data: must in list of list format. [[], []]
        """
        if not isinstance(rows, int) and not isinstance(cols, int):
            raise TypeError("rows and columns must be a integer values")

        self.rows = rows
        self.cols = cols

        if data is None:
            self.data = [[0] * cols for _ in range(rows)]
        else:
            if not all(isinstance(x, list) for x in data):
                raise ValueError("All rows in metric list should be lists")

            if not all(len(data[0]) == len(x) for x in data):
                raise ValueError("All rows must need equal number of columns")

            if not cols == len(data[0]):
                raise ValueError("number of columns must equal to cols")

            if len(data) != rows:
                raise ValueError("number of rows in list must equal to rows")

            self.data = data

    def get(self, r, c):
        if ((r < 0 or r > self.rows - 1) or (c < 0 or c > self.cols - 1)):
            raise Exception("Invalid position!")
        return self.data[r][c]


    def set(self, r, c, v, op='='):
        if ((r < 0 or r > self.rows - 1) or (c < 0 or c > self.cols - 1)):
            raise Exception("Invalid position!")

        if (op == '='): self.data[r][c] = v
        elif (op == '+'): self.data[r][c] += v
        elif (op == '-'): self.data[r][c] -= v
        elif (op == '*'): self.data[r][c] *= v
        elif (op == '/'): self.data[r][c] /= v


    def __add__(m1, m2):
        if (m1.rows != m2.rows or m1.cols != m2.cols): raise Exception("Sizes of both matrix must be equal!")
        m = Matrix(m1.rows, m1.cols)
        addition(m1, m2, m)
        return m

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise Exception("Sizes of both matrix must be equal!")
        m = Matrix(self.rows, self.cols)
        addition(self, -1 * other, m)
        return m

    def __mul__(m1, m2):
        if isinstance(m2, Matrix):
            if (m1.cols != m2.rows): raise Exception("The column count of first matrix must be equal to row count of second matrix!")
            m = Matrix(m1.rows, m2.cols)
            multiply(m1, m2, m)
            return m
        elif isinstance(m2, int) or isinstance(m2, float):
            m = Matrix(m1.rows, m1.cols)
            multiply(m1, m2, m)
            return m
        else:
            raise Exception("Invalid multiplication!")

    def __rmul__(self, other):
        if not isinstance(other, int) and not isinstance(other, float):
            raise ValueError("Invalid multiplication!")

        m = Matrix(self.rows, self.cols)
        multiply(self, other, m)
        return m


    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        if self.rows != other.rows or self.cols != other.cols:
            return False

        for r in range(self.rows):
            for c in range(self.cols):
                if self.get(r, c) != other.get(r, c):
                    return False

        return True

    def isSquare(self):
        return self.rows == self.cols

    def transpose(self):
        m = Matrix(self.cols, self.rows)
        transpose(self, m)
        return m

    def determinant(self):
        return determinant(self)

    def minor(self, r, c):
        if (not self.isSquare()):
            raise Exception("This only for square matrices!")
        if ((r < 0 or r > self.rows - 1) or (c < 0 or c > self.cols - 1)):
            raise Exception("Invalid position!")
        return minor(self, r, c)

    def cofactor(self, r, c):
        if (not self.isSquare()):
            raise Exception("This only for square matrices!")
        if ((r < 0 or r > self.rows - 1) or (c < 0 or c > self.cols - 1)):
            raise Exception("Invalid position!")
        return cofactor(self, r, c)

    def cofactorMatrix(self):
        if (not self.isSquare()):
            raise Exception("This only for square matrices!")

        m = Matrix(self.rows, self.cols)

        for i in range(m.rows):
            for j in range(m.cols):
                m.set(i, j, self.cofactor(i, j))

        return m

    def adjoint(self):
        return self.cofactorMatrix().transpose()

    def inverse(self):
        det = self.determinant()

        if (det == 0):
            raise Exception("The determinant of matrix is zero!")

        return self.adjoint() * (1 / det)