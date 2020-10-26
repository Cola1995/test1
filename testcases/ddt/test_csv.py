import csv
import pytest

def get_data():

    with open("test.csv") as f:
        lst = csv.reader(f)
        my_data = []
        for row in lst:
            my_data.extend(row)
            # print(row)
        return my_data


@pytest.mark.parametrize("name",get_data())
def test01(name):
    print(name)


if __name__ == '__main__':
    pytest.main(["-sv","test_csv.py"])