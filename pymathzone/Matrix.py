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

    def __add__(self):
        # Implement matrix addition logic
        pass

    def __mul__(self):
        # Implement matrix multiplication logic
        pass

    def transpose(self):
        # Implement matrix transpose logic
        pass

    # Other operations (optional)
    def determinant(self):
        # Calculate the determinant of the matrix
        pass

    def inverse(self):
        # Calculate the inverse of the matrix
        pass


n = Matrix(2,2, [1,2])
print(n.data)