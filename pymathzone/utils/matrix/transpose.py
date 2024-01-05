def transpose(m, tm):
    for i in range(m.rows):
        for j in range(m.cols):
            tm.set(j, i, m.get(i, j))