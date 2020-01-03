import unittest
import numpy as np


class TestArrayBasic(unittest.TestCase):

    def test_ndim(self):
        """
        ndim: 次元数
        """
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.ndim, 1)
        self.assertEqual(metrix.ndim, 2)

    def test_shape(self):
        """
        shape: 次元ごとの要素数。新しく追加された次元が `unshift` で追加
        """
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.shape, (3,))
        self.assertEqual(metrix.shape, (2, 3))

    def test_size(self):
        """
        size: 要素数
        """
        vector = np.array([0, 0, 0])
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(vector.size, 3)
        self.assertEqual(metrix.size, 6)

    def test_dtype(self):
        """
        type(): 引数の型を返す
        ndarray.dtype: 配列の要素の型を返す (ndarrayは全要素の型が一緒)
        """
        metrix = np.array([[0, 0, 0], [0, 0, 0]])
        self.assertEqual(type(metrix), np.ndarray)
        self.assertEqual(metrix.dtype, np.int)


if __name__ == '__main__':
    unittest.main()