import unittest
import numpy as np
from numpy.testing import assert_array_equal


class TestArrayEye(unittest.TestCase):

    def test_eye_NxN(self):
        """
        指定次元の単位行列
        """
        metrix = np.eye(3)
        assert_array_equal(metrix, np.array([[1, 0, 0],
                                             [0, 1, 0],
                                             [0, 0, 1]]))

    def test_eye_NxM(self):
        """
        TODO: 解釈を調べる
        """
        metrix = np.eye(2, 3)
        assert_array_equal(metrix, np.array([[1, 0, 0],
                                             [0, 1, 0]]))

    def test_eye_k0(self):
        """
        指定次元の単位行列 (列シフトなし)
        """
        metrix = np.eye(3, k=0)
        assert_array_equal(metrix, np.array([[1, 0, 0],
                                             [0, 1, 0],
                                             [0, 0, 1]]))

    def test_eye_k1(self):
        """
        指定次元の単位行列 (指定分列を右シフト)
        """
        metrix = np.eye(3, k=1)
        assert_array_equal(metrix, np.array([[0, 1, 0],
                                             [0, 0, 1],
                                             [0, 0, 0]]))

    def test_eye_k1m(self):
        """
        指定次元の単位行列 (指定分列を左シフト)
        """
        metrix = np.eye(3, k=-1)
        assert_array_equal(metrix, np.array([[0, 0, 0],
                                             [1, 0, 0],
                                             [0, 1, 0]]))

    def test_eye_rot90(self):
        """
        90度回転 (時計回り方向)
        """
        metrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        assert_array_equal(np.rot90(metrix, k=-1),
                          np.array([[0, 0, 1],
                                    [0, 1, 0],
                                    [1, 0, 0]]))

    def test_eye_rot90m(self):
        """
        90度回転 (反時計回り方向)
        """
        metrix = np.array([[1, 0, 0],
                           [0, 1, 0],
                           [0, 0, 1]])
        assert_array_equal(np.rot90(metrix, k=1),
                          np.array([[0, 0, 1],
                                    [0, 1, 0],
                                    [1, 0, 0]]))


if __name__ == '__main__':
    unittest.main()