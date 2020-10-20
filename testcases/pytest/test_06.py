import pytest

# 类级
class TestCase01(object):


    @classmethod
    def setup_class(cls):
        print("setup_class")

    @classmethod
    def teardown_class(cls):
        print("teardown_class")

    def test01(self):
        print("test01------")

    def test02(self):
        print("test02----------")
if __name__ == '__main__':
    pytest.main(['test_06.py'])