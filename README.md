![screenshot](https://user-images.githubusercontent.com/7298626/46781172-52393900-cd5b-11e8-8c5e-c9689cf30027.png)

# numpy-unittest-100
ユニットテストフレームワークを利用したNumPyの演習問題100



[NumPy公式チュートリアルを効率的に学習する方法](https://note.mu/fookiemonster/n/n7ce86785271f)

## 動作環境
* Python 3系
* PyCharm (推奨)

## テストケース
| テストケース | トピック |
----|---- 
| test_array_basic.py | NumPyの基礎 |
| test_array_broadcast.py | ブロードキャスト |
| test_array_creation.py | 配列の生成 |
| test_array_eye.py | 単位行列 |
| test_array_operation.py | 基本的な操作 |
| test_array_reshape.py | 形状の操作 |
| test_array_select.py | 配列の選択 |
| test_array_slicing.py | インデックス参照とスライス |
| test_array_stack.py | 配列のスタック |
| test_array_stats.py | 統計関数 |
| test_array_ufunc.py | ユニバーサル関数 |

## 使い方
1. このリポジトリをローカルにクローン
1. PyCharm(推奨)でプロジェクトを作成し開く
1. クローン直後は間違ったassert文になっているので全テストが失敗します
1. NumPy公式チュートリアルを読みながら正しいassert文に修正して下さい

## サンプル
~~~
import unittest
import numpy as np
from numpy.testing import assert_array_equal

class TestArrayEye(unittest.TestCase):

    def test_eye_NxN(self):
        metrix = np.eye(3)
        assert_array_equal(metrix, np.array([[1, 0, 0],
                                             [0, 1, 0],
                                             [0, 0, 1]]))

    def test_eye_NxM(self):
        metrix = np.eye(2, 3)
        assert_array_equal(metrix, np.array([[1, 0, 0],
                                             [0, 1, 0]]))
    
    def test_eye_k1(self):
        metrix = np.eye(3, k=1)
        assert_array_equal(metrix, np.array([[0, 1, 0],
                                             [0, 0, 1],
                                             [0, 0, 0]]))

if __name__ == '__main__':
    unittest.main()
~~~

## ライセンス
[MITライセンス](https://github.com/tcnksm/tool/blob/master/LICENCE)

### 参考文献
* NumPy - Quickstart tutorial.
* Rougier - 100 numpy exercises.
* 東大松尾研 - Numpy Test System.