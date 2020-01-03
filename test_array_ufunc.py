import unittest
import numpy as np
from numpy.testing import assert_array_equal


class TestArrayUfunc(unittest.TestCase):

    def test_abs(self):
        """
        絶対値
        """
        vector = np.array([-1, 1, -7])
        assert_array_equal(np.abs(vector), np.array([1, 1, 7]))

    def test_sqrt(self):
        """
        平方根
        """
        vector = np.array([9, 16, 25])
        assert_array_equal(np.sqrt(vector), np.array([3, 4, 5]))

    def test_sort(self):
        """
        ソート
        """
        vector = np.array([1, 6, 2, 3, 8, 1])
        assert_array_equal(np.sort(vector), np.array([1, 1, 2, 3, 6, 8]))

    def test_argsort(self):
        """
        TODO: numpy.argsort 調べる
        """
        vector = np.array([2, 6, 1])
        assert_array_equal(np.argsort(vector), np.array([2, 0, 1]))

    def test_add(self):
        """
        要素同士の足し合わせ
        """
        A = np.array([0, 1, 2])
        B = np.array([2, -1, 4])
        assert_array_equal(np.add(A, B), np.array([2, 0, 6]))

    def test_subtract(self):
        """
        要素同士の引き算
        """
        A = np.array([0, 1, 2])
        B = np.array([2, -1, 4])
        assert_array_equal(np.subtract(A, B), np.array([-2, 2, -2]))

    def test_maximum(self):
        """
        要素同士での最大値
        """
        A = np.array([0, 1, 2])
        B = np.array([2, -1, 4])
        assert_array_equal(np.maximum(A, B), np.array([2, 1, 4]))


if __name__ == '__main__':
    unittest.main()