def multiply(m1, m2, m):
    for i in range(0, m1.rows):
        for j in range(0, m2.cols):
            for k in range(0, m1.cols): # also can use m2.rows (because m1.cols = m2.rows)
                m.data[i][j] += m1.data[i][k] * m2.data[k][j]