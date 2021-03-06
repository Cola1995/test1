import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
class TestUserLogin():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/jpress/user/login")
        self.driver.maximize_window()
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
        username = "admin"
        pwd = "1234556"
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
        self.driver.close()
        self.driver.quit()

if __name__ == '__main__':
    login = TestUserLogin()
    login.test_user_login_success()
