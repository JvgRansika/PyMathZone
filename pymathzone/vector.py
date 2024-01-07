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
            return Vector(addition(self, other))
        else:
            raise ValueError("Invalid addition!")

    def __sub__(self, other):
        if isinstance(other, Vector):
            return self.__add__(-1 * other)
        else:
            raise ValueError("Invalid subtraction!")

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

    def __rmul__(self, other):
        return self.__mul__(other)

    def dot(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self.__mul__(other)
        elif isinstance(other, Vector):
            return dot_multiplication_with_vector(self, other)
        else:
            raise Exception("Invalid dot product")
        
    def magnitude(self):
        return magnitude(self)
    
    def normalize(self):
        return Vector([x / self.magnitude() for x in self.components])
    
    def angle_with(self, other): # returns cos value
        if (not isinstance(other, Vector)):
            raise Exception("Parameter must be a Vector")
        return self.dot(other) / (self.magnitude() * other.magnitude())
    
    def project_onto(self, other): # returns Vector
        if (not isinstance(other, Vector)):
            raise Exception("Parameter must be a Vector")
        return other.normalize() * self.dot(other.normalize())

    def cross(self, other):
        """
        :param other: a vector
        :return: a vector
        """
        if not isinstance(other, Vector):
            raise Exception("Invalid cross product")

        if self.get_dimension() != 3 or other.get_dimension() != 3:
            raise Exception("cross product only defined for three dimensional vectors")

        return Vector(cross_product(self, other))

    def get_dimension(self):
        return len(self.components)
