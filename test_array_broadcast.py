import unittest
import numpy as np
from numpy.testing import assert_array_equal


class TestArrayBroadcast(unittest.TestCase):

    def test_plus(self):
        """
        足し算のブロードキャスト

        np.arrange(6)                   #=> [0, 1, 2, 3, 4, 5]
        np.arrange(6).reshape(2, 3)     #=> [[0, 1, 2], [3, 4, 5]]
        np.arrange(6).reshape(2, 3) + 1 #=> [[1, 2, 3], [4, 5, 6]]

        reshapeの指定が要素数2つなので2次元。(2次元目の要素数, 1次元目の要素数)になる
        """
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector + 1, np.array([[1, 2, 3], [4, 5, 6]]))

    def test_minus(self):
        """
        引き算のブロードキャスト(詳細略)
        """
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector - 1, np.array([[-1, 0, 1], [2, 3, 4]]))

    def test_multi(self):
        """
        掛け算のブロードキャスト(詳細略)
        """
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector * 2, np.array([[0, 2, 4], [6, 8, 10]]))

    def test_square(self):
        """
        指数算のブロードキャスト(詳細略)
        """
        vector = np.arange(6).reshape(2, 3)
        assert_array_equal(vector, np.array([[0, 1, 2], [3, 4, 5]]))
        assert_array_equal(vector ** 2, np.array([[0, 1, 4], [9, 16, 25]]))


if __name__ == '__main__':
    unittest.main()