#!/usr/bin/python3

"""
a function that multiplies 2 matrices by using the module NumPy
"""


import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices (m_a and m_b) using NumPy and returns the resulting product matrix.

    Args:
      m_a: A NumPy array representing the first matrix (m_a).
      m_b: A NumPy array representing the second matrix (m_b).

    Returns:
      A NumPy array representing the product matrix of m_a and m_b.

    Raises:
      ValueError: If the inner dimensions of the matrices are not compatible for multiplication.
  """

    return (np.matmul(m_a, m_b))
