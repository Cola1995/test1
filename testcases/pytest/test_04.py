import  pytest


@pytest.fixture()
def init():
    print("init.....")
    return 1


def test1(init):
    print("test1")

def test2(init):
    print("test02")

if __name__ == '__main__':
    pytest.main(["-sv","test_04.py"])


