import pytest


#模块级/函数的
def setup_module():
    print("setup_moudle")


def teardown_module():
    print("teardown_module")


def setup_function():
    print("setup_function")


def teardown_function():
    print("teardown_function")


def test01():
    print("test01........")


def test02():
    print("test02..........")


if __name__ == '__main__':
    pytest.main(["-sv","test_05.py"])