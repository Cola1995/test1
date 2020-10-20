from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
from testcases.unittest.test_admin_login import TestAdminLogin

class TestArticle(unittest.TestCase):
    # def __init__(self,login):
    #     self.login = login

    def __init__(self, method, login):
        unittest.TestCase.__init__(self, method)
        self.login = login

    def test_add_article(self):
        title = "文章一"
        content = '我的文章内容'
        expected = '文章保存成功。'
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/a/span[1]').click()
        sleep(1)
        # 点击写文章
        self.login.driver.find_element_by_xpath('//*[@id="sidebar-menu"]/li[4]/ul/li[2]/a').click()
        self.login.driver.find_element_by_id('article-title').send_keys(title)
        # //*[@id="cke_1_contents"]/iframe
        frame1 = self.login.driver.find_element_by_xpath('//*[@id="cke_1_contents"]/iframe')

        self.login.driver.switch_to.frame(frame1)

        sleep(1)

        self.login.driver.find_element_by_xpath('/html/body').send_keys(content)
        # 切出
        self.login.driver.switch_to.default_content()

        self.login.driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[1]/div/button[1]').click()

        loc = (By.CLASS_NAME, 'toast-message')

        WebDriverWait(self.login.driver, 5).until(EC.visibility_of_element_located(loc))

        msg = self.login.driver.find_element(*loc).text

        assert msg == expected

    def runTest(self):
        self.test_add_article()

if __name__ == '__main__':
    login = TestAdminLogin()
    login.test_admin_login_success()
    testArticle = TestArticle(login)
    testArticle.test_add_article()
    # unittest.main()


