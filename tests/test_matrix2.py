import sys

sys.path.append('../pymathzone')

from pymathzone.matrix import Matrix

'''
### [Addition]

m1 = Matrix(2,2, [[1,2],[3,4]])
m2 = Matrix(2,2, [[4,3],[2,1]])
m3 = Matrix(2,2, [[1,1], [1,1]])

m4 = m1 + m2 + m3
'''
'''
### [Multiplication]

m1 = Matrix(3,3, [[1,2,1],[3,4,1],[1,1,1]])
m2 = Matrix(3,3, [[4,3,1],[2,1,1],[1,1,1]])

#m1 = Matrix(1,2, [1,2])
#m2 = Matrix(2,1, [[4], [3]])

m4 = m1 * 2
'''

'''
### [Transpose]

m1 = Matrix(2,2, [[1, 2],[3, 4]])

m4 = m1.transpose() 
'''

#print(m4.data)


### [Determinant, Minor, Co-Factor]

m1 = Matrix(2,2, [[-2,3],[4,-9]])
m2 = Matrix(3,3, [[42,1,6],[28,7,4],[14,3,2]])
m3 = Matrix(4,4, [[3,2,5,7], [-1,-4,-3,0], [6,4,2,-1], [2,-1,0,3]])

print(m3.determinant())
#print(m3.minor(0, 3).data)