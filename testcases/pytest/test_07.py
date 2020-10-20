
# https://dl.bintray.com/qameta/generic/io/qameta/allure/allure/2.7.0/
class TestCase01(object):

    def setup(cls):
        print("setup")

    def teardown(cls):
        print("teardown")

    def test01(self):
        print("test01------")

    def test02(self):
        print("test02----------")