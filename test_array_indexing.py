import unittest
import numpy as np
from numpy.testing import assert_array_equal


class TestArrayIndexing(unittest.TestCase):

    def test_indexing_1d(self):
        """
        インデックス: 1次元。listやtupleと同様
        """
        vector = np.arange(10)
        self.assertEqual(vector[0], 0)

    def test_indexing_2d(self):
        """
        インデックス: 多次元
        """
        metrix = np.arange(9).reshape(3, 3)
        self.assertEqual(metrix[0][0], 0)
        self.assertEqual(metrix[0, 0], 0)
        assert_array_equal(metrix[0], np.array([0, 1, 2]))
        assert_array_equal(metrix[1], np.array([3, 4, 5]))
        assert_array_equal(metrix[2], np.array([6, 7, 8]))

    def test_fancy_indexing(self):
        """
        インデックス: シャッフル
        """
        vector = np.array([7, 6, 5])
        assert_array_equal(vector[[2, 0, 1]], np.array([5, 7, 6]))

    def test_indexing_with_boolean_arrays(self):
        """
        条件判断のブロードキャスト
        """
        metrix = np.arange(9).reshape(3, 3)
        assert_array_equal(metrix > 4, np.array([[False, False, False],
                                                 [False, False, True],
                                                 [True, True, True]]))

    def test_indexing_with_selected_elements(self):
        """
        条件判断のブロードキャストかつ、インデックスによるフィルタ
        """
        metrix = np.arange(9).reshape(3, 3)
        assert_array_equal(metrix[metrix > 4], np.array([5, 6, 7, 8]))

    def test_indexing_with_assignments(self):
        """
        条件判定のブロードキャストかつ、インデックスブロードキャストによる
        条件を満たした要素への代入
        """
        metrix = np.arange(9).reshape(3, 3)
        metrix[metrix > 4] = 0
        assert_array_equal(metrix, np.array([[0, 1, 2],
                                             [3, 4, 0],
                                             [0, 0, 0]]))


if __name__ == '__main__':
    unittest.main()