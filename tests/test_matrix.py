import unittest
from pymathzone.matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_add(self):
        matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])
        result = matrix1 + matrix2
        self.assertEqual(result.data, [[8, 10, 12], [14, 16, 18]])

    def test_sub(self):
        matrix1 = Matrix(2, 3, [[1, 2, 3], [4, 5, 6]])
        matrix2 = Matrix(2, 3, [[7, 8, 9], [10, 11, 12]])
        result = matrix1 - matrix2
        self.assertEqual(result.data, [[-6, -6, -6], [-6, -6, -6]])

    def test_init_valid_rows_cols(self):
        matrix = Matrix(2, 3)
        self.assertEqual(matrix.rows, 2)
        self.assertEqual(matrix.cols, 3)
        self.assertEqual(matrix.data, [[0, 0, 0], [0, 0, 0]])

    def test_init_invalid_rows_type(self):
        with self.assertRaises(TypeError):
            Matrix("2", 3)

    def test_init_invalid_cols_type(self):
        with self.assertRaises(TypeError):
            Matrix(2, "3")

    def test_init_valid_data_list(self):
        data = [[1, 2, 3], [4, 5, 6]]
        matrix = Matrix(2, 3, data)
        self.assertEqual(matrix.data, data)

    def test_init_valid_data_single_list(self):
        data = [[1, 2, 3]]
        matrix = Matrix(1, 3, data)
        self.assertEqual(matrix.data, data)

    def test_init_invalid_data_mixed_types(self):
        data = [[1, 2], "hello", [4, 5]]
        with self.assertRaises(ValueError):
            Matrix(3, 2, data)

    def test_init_invalid_data_list_dimensions(self):
        data = [[1, 2], [4]]
        with self.assertRaises(ValueError):
            Matrix(2, 2, data)

    def test_init_invalid_data_list_rows(self):
        data = [[1, 2], [4, 5], [7, 8]]
        with self.assertRaises(ValueError):
            Matrix(2, 2, data)

    def test_init_invalid_data_single_list_length(self):
        data = [[1, 2]]
        with self.assertRaises(ValueError):
            Matrix(1, 3, data)

    def test_init_invalid_data_single_list_rows(self):
        data = [[1, 2, 3]]
        with self.assertRaises(ValueError):
            Matrix(2, 3, data)

    def test_equal_matrices(self):
        matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
        matrix2 = Matrix(2, 2, [[1, 2], [3, 4]])
        self.assertTrue(matrix1 == matrix2)  # Test for equality

    def test_unequal_rows(self):
        matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
        matrix2 = Matrix(2, 3, [[1, 2, 0], [3, 4, 5]])
        self.assertFalse(matrix1 == matrix2)  # Test for inequality (different rows)

    def test_unequal_columns(self):
        matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
        matrix2 = Matrix(2, 3, [[1, 2, 3], [3, 4, 0]])
        self.assertFalse(matrix1 == matrix2)  # Test for inequality (different columns)

    def test_different_values(self):
        matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
        matrix2 = Matrix(2, 2, [[1, 5], [3, 4]])
        self.assertFalse(matrix1 == matrix2)  # Test for inequality (different values)

    def test_different_types(self):
        matrix1 = Matrix(2, 2, [[1, 2], [3, 4]])
        other = "not a matrix"
        self.assertFalse(matrix1 == other)  # Test for inequality (different types)

    # multiplecation
    def test_matrix_by_matrix(self):
        m1 = Matrix(2, 2, [[1, 2], [3, 4]])
        m2 = Matrix(2, 2, [[5, 6], [7, 8]])
        result = m1 * m2
        expected = Matrix(2, 2, [[19, 22], [43, 50]])
        self.assertEqual(result, expected)

    def test_matrix_by_scalar(self):
        m1 = Matrix(2, 2, [[1, 2], [3, 4]])
        result_1 = m1 * 3
        result_2 = 3 * m1  # reverse
        expected = Matrix(2, 2, [[3, 6], [9, 12]])
        self.assertEqual(result_1, expected)
        self.assertEqual(result_2, expected)

    def test_incompatible_dimensions(self):
        m1 = Matrix(2, 2, [[1, 2], [3, 4]])
        m2 = Matrix(3, 2, [[5, 6], [7, 8], [9, 10]])
        with self.assertRaises(Exception) as context:
            result = m1 * m2
        self.assertEqual(str(context.exception),
                         "The column count of first matrix must be equal to row count of second matrix!")

    def test_invalid_multiplication(self):
        m1 = Matrix(2, 2, [[1, 2], [3, 4]])
        with self.assertRaises(Exception) as context:
            result = m1 * "string"
        self.assertEqual(str(context.exception), "Invalid multiplication!")

    def test_matrix_order_change(self):
        m1 = Matrix(2, 2, [[1, 2], [3, 4]])
        m2 = Matrix(2, 2, [[5, 6], [7, 8]])

        result1 = m1 * m2
        result2 = m2 * m1  # Reversed order

        self.assertNotEqual(result1, result2)  # Assert different results
        self.assertEqual(result1.rows, result2.cols)  # Assert dimensions
        self.assertEqual(result1.cols, result2.rows)  # Assert dimensions


if __name__ == '__main__':
    unittest.main()
