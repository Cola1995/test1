import pytest
def test01():
    print("test01111")


def test02():
    print("test022222")

@pytest.mark.do
def test_add():
    print("add")

@pytest.mark.do
def test_sub():
    print("test_sub11111")


if __name__ == '__main__':
    # pytest -s -v test_01.py::test01
    # pytest.main(["-s","-v","test_01.py::test01"])
    # pytest.main(["-s","-v","test_01.py"])
    # pytest -s -v -k add test_01.py
    # pytest.main(["-s","-v","-k","add","test_01.py"])
    # pytest -s -v -m do test_01.py
    pytest.main(["-s", "-v", "-m", "do", "test_01.py"])