import time
import  unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class TestUserRegister(unittest.TestCase):


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://localhost:8080/jpress/user/register")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()

    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://localhost:8080/jpress/user/register")
    #     self.driver.maximize_window()

    def test_register_code_error(self):
        username  = "test01"
        email = "test01@qq.com"
        pwd = 123456
        confirmPwd = 123456
        code =  123
        expected = '验证码不正确'
        self.driver.find_element_by_name("username").send_keys(username)
        self.driver.find_element_by_name("email").send_keys(email)
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        self.driver.find_element_by_name("confirmPwd").send_keys(confirmPwd)
        self.driver.find_element_by_id("captcha").send_keys(code)
        self.driver.find_element_by_class_name("btn").click()
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        # python 的断言
        assert alert.text == expected
        alert.accept()
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()


