def addition(v1, v2):
    """
    :return a tuple with components of result vector
    :param v1:
    :param v2:
    """
    if v1.get_dimension() != v2.get_dimension():
        raise Exception("Both vectors must be same dimension for addition")

    return tuple(x + y for x,y in zip(v1.components, v2.components))