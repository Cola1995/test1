import unittest
import os

class Test1(unittest.TestCase):
    # def setUp(self) -> None:
    #     print("setUp............")
    #
    # def tearDown(self) -> None:
    #     print("tearDown.............")
    def test1(self):
        print("test1...........")
    def test2(self):
        print("test2............")

    @classmethod
    def setUpClass(cls) -> None:
        print("setUpClass.............")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass.............")

if __name__ == '__main__':
    loder = unittest.TestLoader()  # 加载器
    suite = unittest.TestSuite()  # 测试套件
    # suite.addTest(loder.loadTestsFromTestCase(Test1))  # 通过名字加载测试用例
    path = os.path.dirname(os.path.abspath(__file__))   # 通过路径加载测试用例
    suite.addTest(loder.discover(path))



    runner = unittest.TextTestRunner()
    runner.run(suite)


