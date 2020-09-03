import time
import unittest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
import os
from selenium import webdriver


class TestUserLogin(unittest.TestCase):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://10.41.4.47:8080/jpress/user/login")
    #     self.driver.maximize_window()
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://10.41.4.47:8080/jpress/user/login")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

    def test_user_login_error(self):
        """
        登陆失败判断alert值
        """
        username = "admin"
        pwd = "123"
        expected ="用户名或密码不正确"
        self.driver.find_element_by_name("user").send_keys(username)
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_class_name("btn").click()
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected
        alert.accept()
        time.sleep(5)
        # self.driver.close()
        # self.driver.quit()

    def test_user_empty(self):
        """
        测试用户名为空
        """
        username = ""
        pwd ="123"
        expected ="账号不能为空"
        self.driver.find_element_by_name("user").clear()
        self.driver.find_element_by_name("user").send_keys(username)
        self.driver.find_element_by_name("pwd").clear()
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_class_name("btn").click()
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert  = self.driver.switch_to.alert
        assert alert.text == expected
        alert.accept()


    def test_user_login_success(self):
        username = "ma"
        pwd = "qwerdf886."
        expected = "用户中心"
        self.driver.find_element_by_name("user").clear()
        self.driver.find_element_by_name("user").send_keys(username)
        self.driver.find_element_by_name("pwd").clear()
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_class_name("btn").click()
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        title = self.driver.title
        print(title)
        assert title == expected
        time.sleep(5)
if __name__ == '__main__':
    # unittest.main()
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    # report_file = 'ExampleReport.html'
    t = time.time()
    path = os.path.dirname(os.path.dirname(os.path.dirname(__file__))) + "\\reports"
    report_file = path + '\\' + str(t) + "Report.html"
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestUserLogin))
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase1))
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase2))
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase3))

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)