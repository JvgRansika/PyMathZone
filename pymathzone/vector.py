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
        if not isinstance(components, tuple):
            raise ValueError("components must be a tuple")

        self.components = components
