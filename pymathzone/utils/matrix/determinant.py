def _det_of_2x2(m):
    return m.get(0, 0) * m.get(1, 1) - m.get(0, 1) * m.get(1, 0)

def determinant(m):
    if (m.rows == 1): # for 1x1
        return m.get(0, 0)

    if (m.rows == 2): # for 2x2
        return _det_of_2x2(m)

    det = 0

    for i in range(m.cols): # also can use m.rows
        det += m.get(0, i) * m.cofactor(0, i)

    return det
