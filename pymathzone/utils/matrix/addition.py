def addition(m1, m2, m):    
    for i in range(0, m.rows):
        for j in range(0, m.cols):
            m.data[i][j] = m1.data[i][j] + m2.data[i][j]