import unittest
from pymathzone.matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_add(self):
        matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])
        result = matrix1 + matrix2
        self.assertEqual(result.data, [[8, 10, 12], [14, 16, 18]])

    def test_equal(self):
        matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])
        matrix3 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])
        self.assertFalse(matrix1 == matrix2)
        self.assertTrue(matrix2 == matrix3)

        matrix1 = Matrix(1, 3, [1, 2, 3])
        matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])
        self.assertFalse(matrix1==matrix2)


if __name__ == '__main__':
    unittest.main()
