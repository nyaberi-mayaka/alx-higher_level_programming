#!/usr/bin/python3
"""
a function that multiplies 2 matrices
"""

def matrix_mul(m_a, m_b):
    """Multiplies two matrices (m_a and m_b) and returns the resulting product matrix.

    Args:
      m_a: A list of lists representing the first matrix (m_a).
      m_b: A list of lists representing the second matrix (m_b).

    Returns:
      A list of lists representing the product matrix of m_a and m_b.

    Raises:
      TypeError: If either m_a or m_b is not a list, not a list of lists,
                 or contains non-numeric elements.
      ValueError: If either m_a or m_b is empty, or they are not compatible
                 for multiplication (different inner dimensions).
  """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance (m_b, list):
        raise TypeError("m_b must be a list")

    if not all([isinstance(item, list) for item in m_a]):
        raise TypeError("m_a must be a list of lists")

    if not all([isinstance(item, list) for item in m_b]):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")

    if any(not isinstance(element, (float, int)) for row in m_a \
           for element in row):
        raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for element in row:
            if type(element) not in [float, int]:
                raise TypeError("m_b should contain only integers or floats")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")


    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_b) != len(m_a[0]):
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = [[0 for col in range(len(m_b[0]))]
                  for row in range(len(m_a))]
    for row in range(len(m_a)):
        for col in range(len(m_b[0])):
            for item in range(len(m_b)):
                temp_1 = m_a[row][item]
                temp_2 = m_b[item][col]
                if temp_1 != temp_1 or temp_1 == abs(float('inf')):
                    temp_1 = 0
                if temp_2 != temp_2 or temp_2 == abs(float('inf')):
                    temp_2 = 0

                mul_matrix[row][col] += temp_1 * temp_2

    return mul_matrix
