import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from web.podemo1_homework.page.add_member import AddMemberPage
from web.podemo1_homework.page.base import Base


class MainPage(Base):
    url = 'https://work.weixin.qq.com/wework_admin/frame#index'

    def goto_addmenber(self):
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()

        return AddMemberPage(self.driver)

    def goto_contects(self):
        self.find(By.ID, 'menu_contacts').click()

        # 直接点击
        # time.sleep(5)
        # self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()

        # 显示等待，等待某个元素出现，再往后处理
        locator = (By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)')
        element: WebElement = self.wait_for_click(locator)
        element.click()

        return AddMemberPage(self.driver)
