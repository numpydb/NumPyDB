import numpy as np
import unittest

from NumPyDB.src.algebra import Algebra


class TestAlgebra(unittest.TestCase):

    def setUp(self):
        self.vector_a = np.array([1, 2, 3], dtype=float)
        self.vector_dist = 0
        self.vector_b = np.array([4, 5, 6], dtype=float)
        self.vector_sum = np.array([5, 7, 9], dtype=float)
        self.vector_mult_a_b = np.array([4, 10, 18], dtype=float)
        self.k = 2
        self.vector_a_k = np.array([2, 4, 6], dtype=float)

    def test_sum(self):
        result = Algebra.sum(self.vector_a, self.vector_b)
        self.assertEqual(result.all(), self.vector_sum.all())

    def test_mult(self):
        result = Algebra.mult(self.vector_a, self.vector_b)
        self.assertEqual(result.all(), self.vector_mult_a_b.all())

    def test_mult_k(self):
        result = Algebra.mult(self.vector_a, k=self.k)
        self.assertEqual(result.all(), self.vector_a_k.all())

    def test_dist(self):
        result = Algebra.dist(self.vector_a, self.vector_a)
        self.assertEqual(result, self.vector_dist)
