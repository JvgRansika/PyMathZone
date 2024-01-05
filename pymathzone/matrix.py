from .utils.matrix import *


class Matrix:
    def __init__(self, rows: int, cols: int, data=None):
        if not isinstance(rows, int) and not isinstance(cols, int):
            raise TypeError("rows and columns must be a integer values")

        self.rows = rows
        self.cols = cols

        if data is None:
            self.data = [[0] * cols for _ in range(rows)]
        else:
            # ToDo change this logic to match for any type of metrix
            if not all(type(data[0]) == type(x) for x in data):
                raise ValueError("All items in metric list should either integer or list")

            if isinstance(data[0], list):
                if not all(isinstance(x, list) for x in data):
                    raise ValueError("All items in metric list should either integer or list")

                if not all(len(data[0]) == len(x) for x in data):
                    raise ValueError("All rows must need equal number of columns")

                if not cols == len(data[0]):
                    raise ValueError("number of columns must equal to cols")

                if len(data) != rows:
                    raise ValueError("number of rows in list must equal to rows")

            elif len(data) != cols:
                raise ValueError("number of columns must equal to cols")

            elif rows != 1:
                raise ValueError("number of rows in list must equal to rows")

            self.data = data

    def get(self, r, c):
        if ((r < 0 or r > self.rows - 1) or (c < 0 or c > self.cols - 1)):
            raise Exception("Invalid position!")
        if (isinstance(self.data[r], list)):
            return self.data[r][c]
        else:
            return self.data[c]

    def set(self, r, c, v, op='='):
        if ((r < 0 or r > self.rows - 1) or (c < 0 or c > self.cols - 1)):
            raise Exception("Invalid position!")

        if (isinstance(self.data[r], list)):
            if (op == '='): self.data[r][c] = v
            elif (op == '+'): self.data[r][c] += v
            elif (op == '-'): self.data[r][c] -= v
            elif (op == '*'): self.data[r][c] *= v
            elif (op == '/'): self.data[r][c] /= v
        else:
            if (op == '='): self.data[r] = v
            elif (op == '+'): self.data[r] += v
            elif (op == '-'): self.data[r] -= v
            elif (op == '*'): self.data[r] *= v
            elif (op == '/'): self.data[r] /= v

    def __add__(m1, m2):
        if (m1.rows != m2.rows or m1.cols != m2.cols): raise Exception("Sizes of both matrix must be equal!")
        m = Matrix(m1.rows, m1.cols)
        addition(m1, m2, m)
        return m

    def __mul__(m1, m2):
        if (m1.cols != m2.rows): raise Exception("The column count of first matrix must be equal to row count of second matrix!")
        m = Matrix(m1.rows, m2.cols)
        multiply(m1, m2, m)
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

    def transpose(self):
        m = Matrix(self.cols, self.rows)
        transpose(self, m)
        return m

    # Other operations (optional)
    def determinant(self):
        # Calculate the determinant of the matrix
        pass

    def inverse(self):
        # Calculate the inverse of the matrix
        pass