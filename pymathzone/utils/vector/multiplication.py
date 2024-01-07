def multiply_with_scalar(v, s):
    """
    :param v: vector
    :param s: scalar
    :return: tuple with components of result vector
    """
    return tuple(x * s for x in v.components)


def dot_multiplication_with_vector(v1, v2):
    """
    :param v1:
    :param v2:
    :return: a number
    """
    if v1.get_dimension() != v2.get_dimension():
        raise Exception("both vector must be in same dimension for dot product")

    return sum(x * y for x, y in zip(v1.components, v2.components))


def cross_product(v1, v2):
    x1, y1, z1 = v1.components
    x2, y2, z2 = v2.components
    return tuple([y1 * z2 - z1 * y2, z1 * x2 - x1 * z2, x1 * y2 - y1 * x2])
