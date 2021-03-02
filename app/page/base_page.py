"""
base_page.py 基类文件：主要用于初始化driver, 定义find， 常用的最基本的方法
"""
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

logging.basicConfig(level=logging.INFO)
# 也可以配置日志文件，保存日志
# 百度 python logging config


class BasePage:

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, by, locator):
        logging.info(by)
        logging.info(locator)
        return self.driver.find_element(by, locator)

    def find_and_click(self, by, locator):
        logging.info('click')
        self.find(by, locator).click()

    def find_by_scroll(self, text):
        logging.info('find_by_scroll')
        logging.info(text)
        return self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                        f'new UiScrollable(new UiSelector()\
                                        .scrollable(true).instance(0))\
                                        .scrollIntoView(new UiSelector()\
                                        .text("{text}").instance(0));')


    def get_toast_text(self):
        logging.info('get_toast_text')
        result =  self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(result)
        return result