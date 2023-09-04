#!/usr/bin/python3
# 101-lazy_matrix_mul.py
"""a function that multiplies 2 matrices by using the module NumPy"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """a function that multiplies 2 matrices by using the module NumPy

    Args:
        m_a: The first matrix.
        m_b: The second matrix.
    Return:
        multiplies of 2 matrices.
    """

    return (np.matmul(m_a, m_b))
