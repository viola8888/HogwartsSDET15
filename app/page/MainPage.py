from appium.webdriver.common.mobileby import MobileBy

from app.page.AddressListPage import AddressListPage
from app.page.base_page import BasePage


class MainPage(BasePage):
    # def __init__(self, driver):
    #     self.driver = driver
    address_element = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_message(self):
        """
        进入到消息页
        :return:
        """
        pass

    def goto_address(self):
        """
        进入到通讯录页
        :return:
        """
        # self.find(*self.address_element).click()
        self.find_and_click(*self.address_element)
        return AddressListPage(self.driver)
