def addition(m1, m2, m):    
    for i in range(m.rows):
        for j in range(m.cols):
            m.set(i, j,  m1.get(i, j) + m2.get(i, j))