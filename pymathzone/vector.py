from .utils.vector import *


class Vector:
    """
     Vector class representing a vector in n-dimensional space.

     Attributes:
         components: A tuple containing the vector's components.

     Methods:
         __init__(self, components): Initializes the vector with components.
         __str__(self): Returns a human-readable string representation.
         __add__(self, other): Adds two vectors element-wise.
         __sub__(self, other): Subtracts two vectors element-wise.
         __mul__(self, scalar): Multiplies the vector by a scalar.
         magnitude(self): Calculates the magnitude (length) of the vector.
     """

    def __init__(self, components=None):
        """
        Initialize a vector with a tuple
        :param components: a tuple contain vector's components.
        """
        if not components:
            self.components = (0, 0, 0)
        else:
            if not isinstance(components, tuple) and not isinstance(components, list):
                raise ValueError("components must be a tuple")

            self.components = tuple(components)

    def __add__(self, other):
        """
        adding two vectors
        :param other:
        :return: vector
        """
        if isinstance(other, Vector):
            pass
        else:
            raise ValueError("Invalid addition!")

        return Vector(addition(self, other))

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return False
        if self.get_dimension() != other.get_dimension():
            return False

        return self.components == other.components

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return Vector(multiply_with_scalar(self, other))
        else:
            raise Exception("Invalid multiplication")

    def dot(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__mul__(other)
        elif isinstance(other, Vector):
            return dot_multiplication_with_vector(self,other)
        else:
            raise Exception("Invalid dot product")


    def get_dimension(self):
        return len(self.components)
