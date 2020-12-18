import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web.podemo1_homework.page.base import Base


class AddMemberPage(Base):

    def add_member(self, username, acctid, phonenum):

        username_is = (By.ID, 'username')
        self.wait_for_click(username_is)

        self.find(By.ID, 'username').send_keys(username)
        self.find(By.ID, 'memberAdd_acctid').send_keys(acctid)
        self.find(By.ID, 'memberAdd_phone').send_keys(phonenum)
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

        return True

    def get_member(self, value):
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute('title') for element in contactlist]

            if value in titlelist:
                return True

            result: str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, '.ww_commonImg_PageNavArrowRightNormal').click()
