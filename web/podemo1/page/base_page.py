# 基类： 最基本的方法，driver实例化  find()等
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver: webdriver = None):
        # driver:webdriver
        base_url = ''
        if driver == None:
            # 第一次初始化
            options = Options()
            options.debugger_address = '127.0.0.1:9222'
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(10)
        else:
            # 进行页面跳转的操作
            self.driver = driver

        if base_url != "":
            self.driver.get(base_url)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def finds(self, by, locator):
        return self.driver.find_elements(by, locator)

    def wait_for_click(self, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return element
