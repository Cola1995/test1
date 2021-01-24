from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from util.util import get_code

class TestAdminLogin(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://10.41.4.47:8080/jpress/admin/login")
        self.driver.maximize_window()
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
        pwd = "admin123!"
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
#
# if __name__ == '__main__':
#     login = TestAdminLogin()
#     login.test_admin_login_success()