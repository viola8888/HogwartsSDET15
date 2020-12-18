import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from web.podemo.login_page import LoginPage
from web.podemo.register_page import RegisterPage


class IndexPage:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://work.weixin.qq.com/')
        self.driver.implicitly_wait(5)

    def goto_login(self):
        # click login
        self.driver.find_element(By.CSS_SELECTOR, '.index_top_operation_loginBtn').click()
        # return LoginPage
        return LoginPage(self.driver)

    def goto_register(self):
        self.driver.find_element(By.CSS_SELECTOR, '.index_head_info_pCDownloadBtn').click()
        return RegisterPage(self.driver)
