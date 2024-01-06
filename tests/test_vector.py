import unittest
from pymathzone.vector import Vector


class TestVector(unittest.TestCase):
    def test_add_same_dimension(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([4, 5, 6])
        result = v1 + v2
        self.assertEqual(result.components, (5, 7, 9))

    def test_add_different_dimensions(self):
        v1 = Vector([1, 2])
        v2 = Vector([3, 4, 5])
        with self.assertRaises(Exception) as context:
            v1 + v2
        self.assertEqual(str(context.exception), "Both vectors must be same dimension for addition")

    def test_add_non_vector(self):
        v1 = Vector([1, 2])
        with self.assertRaises(ValueError) as context:
            v1 + 5
        self.assertEqual(str(context.exception), "Invalid addition!")

    def test_add_zero_vector(self):
        v1 = Vector([1, 2, 3])
        zero_vector = Vector([0, 0, 0])
        result = v1 + zero_vector
        self.assertEqual(result, v1)

    def test_add_negative_vector(self):
        v1 = Vector([1, 2, 3])
        v2 = Vector([-1, -2, -3])
        result = v1 + v2
        self.assertEqual(result.components, (0, 0, 0))


if __name__ == '__main__':
    unittest.main()
