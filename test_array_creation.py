import unittest
import numpy as np
from numpy.testing import assert_array_equal


class TestArrayCreation(unittest.TestCase):

    def test_from_list(self):
        """
        listからndarrayを作成する
        """
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(metrix.shape, (2, 3))

    def test_from_tuple(self):
        """
        tupleからndarrayを作成する
        """
        metrix = np.array(((0, 0, 0), (0, 0, 0)))
        self.assertEqual(metrix.shape, (2, 3))

    def test_zeros_vector(self):
        """
        ゼロ埋めの一次元ndarrayを作成する
        """
        vector = np.zeros(5)
        assert_array_equal(vector, np.array([0, 0, 0, 0, 0]))

    def test_zeros_metrix(self):
        """
        ゼロ埋めの二次元ndarrayを作成する。5つの要素があるarrayが2つのarray
        """
        metrix = np.zeros((2, 5))
        assert_array_equal(metrix, np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]))

    def test_ones_vector(self):
        """
        1埋めの一次元ndarrayを作成する
        """
        vector = np.ones(5)
        assert_array_equal(vector, np.array([1, 1, 1, 1, 1]))

    def test_ones_metrix(self):
        """
        1埋めの二次元ndarrayを作成する。5つの要素があるarrayが2つのarray
        """
        metrix = np.ones((2, 5))
        assert_array_equal(metrix, np.array([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))

    def test_empty(self):
        """
        埋めの二次元ndarrayを作成する。5つの要素があるarrayが2つのarray
        その形を調べる

        TODO: ndarray.empty について調べる
        """
        metrix = np.empty((2, 5))
        self.assertEqual(metrix.shape, (2, 5))

    def test_arange_to(self):
        """
        順数のndarrayを作成する(終了のみ指定)
        """
        vector = np.arange(5)
        assert_array_equal(vector, np.array([0, 1, 2, 3, 4]))

    def test_arange_from_to(self):
        """
        順数のndarrayを作成する(開始と終了を指定)
        """
        vector = np.arange(0, 5)
        assert_array_equal(vector, np.array([0, 1, 2, 3, 4]))

    def test_arange_with_step(self):
        """
        順数のndarrayを作成する(開始と終了とステップを指定)
        """
        vector = np.arange(0, 10, 2)
        assert_array_equal(vector, np.array([0, 2, 4, 6, 8]))

    def test_linspace(self):
        """
        順数のndarrayを作成する(開始と終了とステップを指定)
        """
        vector = np.linspace(0, 2, 5)
        assert_array_equal(vector, np.array([0., 0.5, 1.0, 1.5, 2.0]))

    def test_eye(self):
        """
        指定次元の単位行列を作成
        """
        metrix = np.eye(3)
        assert_array_equal(metrix, np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))

    def test_identify(self):
        """
        指定次元の単位行列を作成
        """
        metrix = np.identity(3)
        assert_array_equal(metrix, np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))


if __name__ == '__main__':
    unittest.main()