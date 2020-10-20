import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from util.util import get_code
from lib.HTMLTestRunner import HTMLTestRunner
import os

class TestAdminLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://localhost:8080/jpress/admin/login')
        cls.driver.maximize_window()
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://localhost:8080/jpress/admin/login")
    #     self.driver.maximize_window()
    def test_admin_login_code_empty(self):
        username = 'admin'
        # pwd  = "admin123!"
        pwd = "123456"
        expected = "验证码不能为空"
        self.driver.find_element_by_name("user").send_keys(username)
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_class_name("btn").click()
        WebDriverWait(self.driver,5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        assert alert.text == expected
        alert.accept()
        # time.sleep(5)
    def test_admin_login_success(self):
        username = "admin"
        # pwd = "admin123!"
        pwd = "123456"
        expected = "JPress后台"
        code = get_code(self.driver,"captchaImg")
        self.driver.find_element_by_name("user").clear()
        self.driver.find_element_by_name("user").send_keys(username)
        self.driver.find_element_by_name("pwd").clear()
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_name("captcha").send_keys(code)
        self.driver.find_element_by_class_name("btn").click()
        WebDriverWait(self.driver, 5).until(EC.title_is(expected))
        title = self.driver.title
        assert title == expected
        time.sleep(3)
        # self.driver.close()
        # self.driver.quit()

    @classmethod
    def tearDownClass(cls) -> None:
        # print("tearDownClass.............")
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    report_title = 'Example用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'ExampleReport.html'

    path = os.path.dirname(os.path.dirname(__file__)) + '\\reports\\ExampleReport.html'
    print(path)
    path = r"C:\Users\99157\PycharmProject\test1\reports\ExampleReport.html"
    testsuite = unittest.TestSuite()

    testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestAdminLogin))

    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase1))
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase2))
    # testsuite.addTest(unittest.TestLoader().loadTestsFromTestCase(ExampleCase3))

    with open(path, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(testsuite)
