import yaml
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from frame.hand_black import handle_black

# from frame.singleton import singleton


# @singleton
class BasePage:
    black_list = [(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/iv_close']")]
    max_num = 3
    error_num = 0
    def __init__(self, driver: WebDriver=None):
        """
        初始化应用
        """
        if driver is None:
            caps = {}
            caps['platformName'] = "android"
            caps['appPackage'] = 'com.xueqiu.android'
            caps['appActivity'] = '.common.MainActivity'
            caps["deviceName"] = "hogwarts"
            caps['noReset'] = 'true'
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
            self.driver.implicitly_wait(20)
        else:
            self.driver = driver


    # def find(self, by, locator=None):
    #     """
    #     查找元素
    #     :return:
    #     """
    #
    #     try:
    #         if locator is None:
    #             # 如果传的元素是一个，只有 by
    #             result = self.driver.find_element(*by)
    #         else:
    #             # 如果传的元素是二个，既有 by  ，又有 locator
    #             result = self.driver.find_element(by, locator)
    #         self._error_num = 0
    #         return result
    #     # 捕获黑名单中的元素
    #     except Exception as e:
    #         # 超过最大查找次数
    #         if self._error_num > self._max_num:
    #             raise e
    #         self._error_num += 1
    #         # 从黑名单中遍历元素，一次进行处理
    #         for black_ele in self._black_list:
    #             ele = self.driver.find_elements(*black_ele)
    #             if len(ele) > 0:
    #                 ele[0].click()
    #                 # 处理完黑名单后，再次查找原来的元素
    #                 return self.find(by, locator)
    #         raise e

    #   使用装饰器
    @handle_black
    def find(self, by, locator=None):
        """
        查找元素
        :return:
        """

        if locator is None:
            # 如果传的元素是一个，只有 by
            result = self.driver.find_element(*by)
        else:
            # 如果传的元素是二个，既有 by  ，又有 locator
            result = self.driver.find_element(by, locator)

        return result

    def parse_ymal(self, path, func_name):
        with open(path, encoding="utf-8") as f:
            data = yaml.load(f)
        self.parse(data[func_name])

    def parse(self,steps):
        for step in steps:
            if 'click' == step['action']:
                self.find(step['by'], step['locator']).click()
            elif 'send' == step['action']:
                self.find(step['by'], step['locator']).send_keys(step["content"])