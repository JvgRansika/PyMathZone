import sys

sys.path.append('../pymathzone')

from pymathzone.Matrix import Matrix

'''
### [Addition]

m1 = Matrix(2,2, [[1,2],[3,4]])
m2 = Matrix(2,2, [[4,3],[2,1]])
m3 = Matrix(2,2, [[1,1], [1,1]])

m4 = m1 + m2 + m3
'''

### [Multiplication]

#m1 = Matrix(3,3, [[1,2,1],[3,4,1],[1,1,1]])
#m2 = Matrix(3,3, [[4,3,1],[2,1,1],[1,1,1]])

m1 = Matrix(1,2, [1,2])
m2 = Matrix(2,1, [[4], [3]])

m4 = m1 * m2

print(m4.data)