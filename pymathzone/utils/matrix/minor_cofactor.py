import math

def minor(m, r, c):
    Matrix = type(m)

    matrix = Matrix(m.rows - 1, m.cols - 1)

    for i in range(m.rows):
        for j in range(m.cols):
            if (i == r or j == c):
                continue

            ii = i
            jj = j

            if i > r: ii -= 1
            if j > c: jj -= 1

            matrix.set(ii, jj, m.get(i, j))

    return matrix.determinant()

def cofactor(m, r, c):
    return int(math.pow(-1, r + c)) * m.minor(r, c)