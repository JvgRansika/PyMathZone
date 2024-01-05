def multiply(m1, m2, m):
    for i in range(m1.rows):
        for j in range(m2.cols):
            for k in range(m1.cols): # also can use m2.rows (because m1.cols = m2.rows)
                m.set(i, j, m1.get(i, k) * m2.get(k, j), '+')