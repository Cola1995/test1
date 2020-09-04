import pytest

class Test01(object):


    def test01(self):
        print("test01111")

    def test02(self):
        print("test022222")


if __name__ == '__main__':
    pytest.main(["-s","-v","test_01.py"])