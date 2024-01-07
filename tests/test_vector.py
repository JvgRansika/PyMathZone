import unittest

import sys
sys.path.append('../pymathzone')

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

    # subtraction
    def test_subtraction_with_vector(self):
        vector1 = Vector((5, 3))
        vector2 = Vector((2, 1))
        result = vector1 - vector2
        expected = Vector((3, 2))
        self.assertEqual(result, expected)

    def test_subtraction_with_scalar(self):
        vector = Vector((4, 2))
        with self.assertRaises(ValueError) as context:
            vector - 5
        self.assertEqual(str(context.exception), "Invalid subtraction!")

    def test_subtraction_with_invalid_type(self):
        vector = Vector((1, 2))
        with self.assertRaises(ValueError) as context:
            vector - "hello"
        self.assertEqual(str(context.exception), "Invalid subtraction!")

    def test_multiplication_with_scalar(self):
        vector = Vector((2, 3))
        result = vector * 2
        expected = Vector((4, 6))
        self.assertEqual(result, expected)

    def test_multiplication_with_negative_scalar(self):
        vector = Vector((5, 1))
        result = vector * -3
        expected = Vector((-15, -3))
        self.assertEqual(result, expected)

    def test_multiplication_with_float_scalar(self):
        vector = Vector((1.5, 2.4))
        result = vector * 0.5
        expected = Vector((0.75, 1.2))
        self.assertEqual(result, expected)

    def test_multiplication_with_invalid_type(self):
        vector = Vector((1, 2))
        with self.assertRaises(Exception) as context:
            vector * "hello"
        self.assertEqual(str(context.exception), "Invalid multiplication")

    def test_multiplication_with_vector(self):
        vector1 = Vector((1, 2))
        vector2 = Vector((3, 4))
        with self.assertRaises(Exception) as context:
            vector1 * vector2
        self.assertEqual(str(context.exception), "Invalid multiplication")

    def test_dot_with_scalar(self):
        vector = Vector((2, 3))
        result = vector.dot(5)
        expected = Vector((10, 15))  # Assuming __mul__ handles scalar multiplication
        self.assertEqual(result, expected)

    def test_dot_with_vector(self):
        vector1 = Vector((1, 2))
        vector2 = Vector((3, 4))
        result = vector1.dot(vector2)
        expected = 11  # Assuming dot_multiplication_with_vector calculates correctly
        self.assertEqual(result, expected)

    def test_dot_with_different_dimension_vectors(self):
        vector1 = Vector((1, 2))
        vector2 = Vector((3, 4, 5))
        with self.assertRaises(Exception) as context:
            vector1.dot(vector2)
        self.assertEqual(str(context.exception), "both vector must be in same dimension for dot product")

    def test_dot_with_invalid_type(self):
        vector = Vector((1, 2))
        with self.assertRaises(Exception) as context:
            vector.dot("hello")
        self.assertEqual(str(context.exception), "Invalid dot product")

    def test_magnitude(self):
        vector = Vector((1, 2, 2))
        result = vector.magnitude()
        expected = 3.0
        self.assertEqual(result, expected)

    def test_normalize_vector(self):
        vector = Vector((0, 0, 1))
        result = vector.normalize()
        expected = Vector((0, 0, 1))
        self.assertEqual(result, expected)

    def test_angle_with_another_vector(self):
        vector1 = Vector((2, 0, 0))
        vector2 = Vector((0, 0, 3))
        result = vector1.angle_with(vector2)
        expected = 0.0
        self.assertEqual(result, expected)

    def test_projection_onto_another_vector(self):
        vector1 = Vector((2, 0, 2))
        vector2 = Vector((3, 0, 0))
        result = vector1.project_onto(vector2)
        expected = Vector((2, 0, 0))
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
