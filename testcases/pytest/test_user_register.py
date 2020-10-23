import time
import pytest

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from util import util


class TestUserRegister(object):
    # def __init__(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://localhost:8080/jpress/user/register")
    #     self.driver.maximize_window()
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://10.41.4.47:8080/jpress/user/register")
        self.driver.maximize_window()
    def teardown_class(self):
        self.driver.close()
        self.driver.quit()

    def test1_register_code_error(self):
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
        # time.sleep(5)
        # self.driver.close()
        # self.driver.quit()

        # 测试成功
    def test2_register_ok(self):
        username = util.gen_random_str()
        email = username + '@qq.com'
        pwd = '123456'
        confirmPwd = '123456'
        # 自动获取
        captcha = ''
        expected = '注册成功，点击确定进行登录。'

        # 输入用户名
        username_elem = self.driver.find_element_by_name('username')
        username_elem.clear()
        username_elem.send_keys(username)

        # email
        email_elem = self.driver.find_element_by_name('email')
        email_elem.clear()
        email_elem.send_keys(email)
        # 密码
        self.driver.find_element_by_name('pwd').clear()
        self.driver.find_element_by_name('pwd').send_keys(pwd)
        # 确认密码
        self.driver.find_element_by_name('confirmPwd').clear()
        self.driver.find_element_by_name('confirmPwd').send_keys(confirmPwd)
        # 自动识别验证码
        captcha = util.get_code(self.driver, 'captchaimg')
        # 输入验证码
        self.driver.find_element_by_name('captcha').clear()
        self.driver.find_element_by_name('captcha').send_keys(captcha)
        # 点击注册
        self.driver.find_element_by_class_name('btn').click()

        # 等待alert出现
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert

        # 验证
        assert alert.text == expected
        # self.assertEqual(alert.text, expected)
        alert.accept()


if __name__ == '__main__':
    pytest.main(['test_user_register.py'])




