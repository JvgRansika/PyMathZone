def addition(m1, m2, m):    
    for i in range(0, m.rows):
        for j in range(0, m.cols):
            m.set(i, j,  m1.get(i, j) + m2.get(i, j))