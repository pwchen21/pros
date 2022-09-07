import pytest

def test_a(): # test開頭的測驗函式
     print("------->test_a")
     assert 1 # 斷言成功

def test_b():
     print("------->test_b")
     assert 0 # 斷言失敗

if __name__ == '__main__':
        pytest.main(['-s', 'class01.py'])