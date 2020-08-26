import os

from selenium import webdriver
import time
from util import util
from testcases import testcase1
from testcases.base.test_user_register import TestUserRegister
from testcases.base.test_user_login import TestUserLogin
from testcases.base.test_admin_login import TestAdminLogin
from testcases.base.test_article import TestArticle
from testcases.base.test_admin_add_category import TestAdminAddCategory

if __name__ == '__main__':
    # browser = webdriver.Chrome()
    # browser.get("http://localhost:8080/jpress/user/register")
    # browser.minimize_window()
    # print(util.get_code(browser, "captchaimg"))

    # print(util.gen_random_str())
    # t1 = TestUserRegister()
    # t1.test_register_code_error()
    # t1  = TestUserLogin()
    # t1.test_user_login_error()
    # t1.test_user_empty()
    # t1.test_user_login_success()

    # t1 = TestAdminLogin()
    # t1.test_admin_login_code_empty()
    # t1.test_admin_login_success()

    # 测试添加分类
    # login = TestAdminLogin()
    # login.test_admin_login_success()
    # t1 = TestAdminAddCategory(login)
    # t1.test_add_catagory_error()

    login = TestAdminLogin()
    login.test_admin_login_success()
    t1 = TestArticle(login)
    t1.test_add_article()


