import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
class TestUserLogin():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://10.41.4.47:8080/jpress/user/login")
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
        self.driver.close()
        self.driver.quit()