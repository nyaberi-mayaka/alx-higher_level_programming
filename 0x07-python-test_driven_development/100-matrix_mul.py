#!/usr/bin/python3
"""Module that multiplies 2 matrices:"""


def matrix_mul(m_a=[[]], m_b=[[]]):
    """Multiplies two matrices and return the resulting matrix.
    Args:
        m_a (list): Matrix represented as a list of lists.
        m_b (list): Matrix represented as a list of lists.
    Raises:
        TypeError: If m_a or m_b is not a list of lists, or if one of its
                  elements is not an integer or a float.
                  Also raised if m_a and m_b are not rectangles or if m_a
                  and m_b can't be multiplied.
        ValueError: If m_a or m_b is an empty list.
    Converts:
        NaN and abs(infinity) to 0
    Returns:
        list: Matrix representing the product of m_a and m_b.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all([isinstance(item, list) for item in m_a]):
        raise TypeError("m_a must be a list of lists")

    if not all([isinstance(item, list) for item in m_b]):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not all([item for item in m_a]):
        raise ValueError("m_a can't be empty")

    if not m_b or not all([item for item in m_b]):
        raise ValueError("m_b can't be empty")

    if not all([all([isinstance(n, (float, int)) for n in i]) for i in m_a]):
        raise TypeError("m_a should contain only integers or floats")

    if not all([all([isinstance(n, (float, int)) for n in i]) for i in m_b]):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    row_a = len(m_a)
    col_a = len(m_a[0])
    row_b = len(m_b)
    col_b = len(m_b[0])

    if row_b != col_a:
        raise ValueError("m_a and m_b can't be multiplied")

    mul = [[0 for item in range(col_b)] for i in range(row_a)]

    for i in range(row_a):
        for j in range(col_b):
            for k in range(row_b):
                temp_1 = m_a[i][k]
                temp_2 = m_b[k][j]

                if temp_1 != temp_1 or temp_1 == abs(float('inf')):
                    temp_1 = 0

                if temp_2 != temp_2 or temp_2 == abs(float('inf')):
                    temp_2 = 0
                mul[i][j] += temp_2 * temp_1

    return (mul)
